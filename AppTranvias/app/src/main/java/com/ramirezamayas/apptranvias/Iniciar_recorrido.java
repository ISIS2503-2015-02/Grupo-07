package com.ramirezamayas.apptranvias;

import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.widget.TextView;
import android.widget.Toast;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.client.methods.HttpPut;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicHeader;
import org.apache.http.params.HttpConnectionParams;
import org.apache.http.protocol.HTTP;
import org.json.JSONObject;

import java.io.InputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;


public class Iniciar_recorrido extends ActionBarActivity {

    //TextView para comunicar el reporte de información
    private TextView textView;

    //GPSTracker para obtener localización
    private GPSTracker gpsTracker;

    //URL recorridos Movibus
    private String urlRecorridos = "recorridosTranvia/";

    //URL coordenadas Movibus
    private String urlCoordenadas = "coordenadasTranvia/";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        //Instanciación del GPSTracker
        gpsTracker = new GPSTracker(this);
        //Display del TextView
        textView = new TextView(this);
        textView.setTextSize(30);
        setContentView(textView);
        //Ejecución actividad asincrónica de reporte de posición
        MainActivity.getTranvia().setUltimo_recorrido(MainActivity.getTranvia().getUltimo_recorrido() + 1);
        new EnviarReportePosicionTask().execute();
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu items for use in the action bar
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu_main, menu);
        return super.onCreateOptionsMenu(menu);
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle presses on the action bar items
        switch (item.getItemId()) {
            case R.id.action_search:
                openSearch();
                return true;
            case R.id.action_settings:
                openSettings();
                return true;
            default:
                return super.onOptionsItemSelected(item);
        }
    }

    //Tarea asincrónica que crea un recorrido y reporta posición cada 20 segundos
    private class EnviarReportePosicionTask extends AsyncTask<Void, String, Void> {

        @Override
        //Metodo ejecutable de AsyncTask
        protected Void doInBackground(Void... nada) {
            try {
                //Setup de la conexión
                URL url_recorrido = new URL(MainActivity.IP + MainActivity.PUERTO + urlRecorridos);
                HttpURLConnection con_recorrido = (HttpURLConnection)url_recorrido.openConnection();
                con_recorrido.setDoOutput(true);
                con_recorrido.setDoInput(true);
                con_recorrido.setRequestProperty("Content-Type", "application/json");
                con_recorrido.setRequestProperty("Authorization", "Token " + Login.auth_token);
                con_recorrido.setRequestMethod("POST");
                //Setup del JSON
                JSONObject recorrido   = new JSONObject();
                recorrido.put("identificador", MainActivity.getTranvia().getUltimo_recorrido());
                recorrido.put("tranvia", MainActivity.getTranvia().getPlaca());
                recorrido.put("linea", MainActivity.getTranvia().getLinea());
                recorrido.put("conductor", MainActivity.getTranvia().getConductor_actual());
                //Incorporación del JSON a la conexión
                OutputStreamWriter out_recorrido = new OutputStreamWriter(con_recorrido.getOutputStream());
                out_recorrido.write(recorrido.toString());
                out_recorrido.flush();
                out_recorrido.close();
                //Verificación estado y cierre de conexión
                int status_request_recorrido = con_recorrido.getResponseCode();
                Log.d("status_req_recorrido",Integer.toString(status_request_recorrido));
                con_recorrido.disconnect();
                //Ciclo para el reporte de posición
                while (MainActivity.darDetenerRecorrido()){
                    //Posición a reportar
                    double lat = gpsTracker.getLatitude();
                    double lon = gpsTracker.getLongitude();
                    //Setup de la conexión
                    URL url_coordenadas = new URL(MainActivity.IP + MainActivity.PUERTO + urlCoordenadas);
                    HttpURLConnection con_coordenadas = (HttpURLConnection)url_coordenadas.openConnection();
                    con_coordenadas.setDoOutput(true);
                    con_coordenadas.setDoInput(true);
                    con_coordenadas.setRequestProperty("Content-Type", "application/json");
                    con_coordenadas.setRequestProperty("Authorization", "Token " + Login.auth_token);
                    con_coordenadas.setRequestMethod("POST");
                    //Setup del JSON
                    JSONObject coordenada   = new JSONObject();
                    recorrido.put("latitud", lat);
                    recorrido.put("longitud", lon);
                    recorrido.put("tranvia",MainActivity.getTranvia().getPlaca());
                    recorrido.put("recorrido", MainActivity.getTranvia().getUltimo_recorrido());
                    //Incorporación del JSON a la conexión
                    OutputStreamWriter out_coordenadas = new OutputStreamWriter(con_coordenadas.getOutputStream());
                    out_coordenadas.write(recorrido.toString());
                    out_coordenadas.flush();
                    out_coordenadas.close();
                    //Verificación estado y cierre de conexión
                    int status_request_coordenadas = con_coordenadas.getResponseCode();
                    Log.d("status_req_coordenadas",Integer.toString(status_request_recorrido));
                    con_coordenadas.disconnect();

                    if(status_request_recorrido == 201 && status_request_coordenadas ==201){
                        publishProgress("Reportando posicion (lat = " + lat + ", lon = " + lon + ")");
                    }

                    Log.d("Status", String.valueOf("entró"));
                    try {
                        Thread.sleep(20000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    Log.d("Status", String.valueOf("salió"));
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
            publishProgress("Estamos teniendo dificultades al reportar la posición. Por favor intente de nuevo!");
            return null;
        }

        @Override
        //Actualización del TextView de UI
        protected void onProgressUpdate(String... params) {
            textView.setText(params[0]);
        }
    }

    //Toast search Action_bar
    private void openSearch() {
        Toast.makeText(this, "Search button pressed", Toast.LENGTH_SHORT).show();
    }

    //Toast settings Action_bar
    private void openSettings() {
        Toast.makeText(this, "Settings button pressed", Toast.LENGTH_SHORT).show();
    }
}
