package com.ramirezamayas.appmovibus;

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


public class Iniciar_recorrido extends ActionBarActivity {

    //TextView para comunicar el reporte de información
    private TextView textView;

    //GPSTracker para obtener localización
    private GPSTracker gpsTracker;

    //Tarea asincrónica que crea un recorrido y reporta posición cada 20 segundos
    private class EnviarReportePosicionTask extends AsyncTask<Void, String, Void> {

        @Override
        //Metodo ejecutable de AsyncTask
        protected Void doInBackground(Void...param ) {
            try {
                HttpClient client = new DefaultHttpClient();
                HttpConnectionParams.setConnectionTimeout(client.getParams(), 1000);
                HttpResponse response;
                JSONObject json_recorrido = new JSONObject();
                JSONObject json_posicion = new JSONObject();

                Log.d("Status", String.valueOf(MainActivity.darIdRecorrido()));

                HttpPost put_recorrido = new HttpPost("http://10.0.2.2:9345/recorridosMovibus/");
                json_recorrido.put("identificador", String.valueOf(MainActivity.darIdRecorrido()));
                json_recorrido.put("reserva", MainActivity.darIdReserva());
                json_recorrido.put("movibus", MainActivity.darIdMovibus());
                json_recorrido.put("conductor", "1");
                StringEntity se_recorrido = new StringEntity( json_recorrido.toString());
                se_recorrido.setContentType(new BasicHeader(HTTP.CONTENT_TYPE, "application/json"));
                put_recorrido.setEntity(se_recorrido);
                response = client.execute(put_recorrido);
                if(response!=null){
                    InputStream in = response.getEntity().getContent();
                }
                int d2 = response.getStatusLine().getStatusCode();
                Log.d("Status", String.valueOf(d2));

                while (MainActivity.darDetenerRecorrido()){

                    client = new DefaultHttpClient();
                    HttpConnectionParams.setConnectionTimeout(client.getParams(), 1000);

                    double lat = gpsTracker.getLatitude();
                    double lon = gpsTracker.getLongitude();

                    HttpPost put_posicion = new HttpPost("http://10.0.2.2:9345/coordenadasMovibus/");
                    json_posicion.put("latitud", lat);
                    json_posicion.put("longitud", lon);
                    json_posicion.put("movibus", MainActivity.darIdMovibus());
                    json_posicion.put("recorrido", String.valueOf(MainActivity.darIdRecorrido()));
                    StringEntity se_posicion = new StringEntity( json_posicion.toString());
                    se_posicion.setContentType(new BasicHeader(HTTP.CONTENT_TYPE, "application/json"));
                    put_posicion.setEntity(se_posicion);
                    response = client.execute(put_posicion);
                    if(response!=null){
                        InputStream in = response.getEntity().getContent();
                    }
                    int d1 = response.getStatusLine().getStatusCode();
                    Log.d("Status", String.valueOf(d1));

                    if(d1 > 199 && d1 <300 && d1 > 199 && d1 <300){
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

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        Intent intent = getIntent();

        gpsTracker = new GPSTracker(this);

        textView = new TextView(this);
        textView.setTextSize(30);
        setContentView(textView);

        MainActivity.aumentarIdRecorrido();
        new EnviarReportePosicionTask().execute();
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
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
}

