package com.ramirezamayas.appvcub;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.StrictMode;
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

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;


public class Reportar_devolucion extends ActionBarActivity {

    private TextView textView;

    //URL recuperacion info estacion
    private String urlDevolucionEstacion = "estaciones/";

    //URL recuperacion info vcub
    private String urlDevolucionVcub = "vcub/";

    //ID vcub a devolver
    private String idVcub;

    //Vcub del app
    private Vcub vcub;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        //Recuperación info vcub desde Main
        Intent intent = getIntent();
        idVcub = intent.getStringExtra(MainActivity.EXTRA_MESSAGE);
        textView = new TextView(this);
        textView.setTextSize(30);
        setContentView(textView);
        //Ejecución actividad asincrónica de reporte de devolución
        MainActivity.getEstacion().setCap_actual(MainActivity.getEstacion().getCap_actual() + 1);
        new EnviarReporteDevolucion().execute(idVcub);
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

    private class EnviarReporteDevolucion extends AsyncTask<String, Void, String> {
        @Override
        protected String doInBackground(String... message) {
            try {
                //Setup de la conexión
                URL url_devolucion = new URL(MainActivity.IP + MainActivity.PUERTO + urlDevolucionEstacion);
                HttpURLConnection con_devolucion = (HttpURLConnection)url_devolucion.openConnection();
                con_devolucion.setDoOutput(true);
                con_devolucion.setDoInput(true);
                con_devolucion.setRequestProperty("Content-Type", "application/json");
                con_devolucion.setRequestProperty("Accept", "application/json");
                con_devolucion.setRequestProperty("Authorization", "Token " + Login.auth_token);
                con_devolucion.setRequestMethod("PUT");
                //Setup del JSON
                JSONObject devolucion   = new JSONObject();
                devolucion.put(Estacion.NOMBRE, MainActivity.getEstacion().getNombre());
                devolucion.put(Estacion.FECHA_CONSTRUCCION,MainActivity.getEstacion().getFecha_construccion());
                devolucion.put(Estacion.CAP_ACTUAL,MainActivity.getEstacion().getCap_actual());
                devolucion.put(Estacion.CAP_MAX,MainActivity.getEstacion().getCap_max());
                devolucion.put(Estacion.LAT,MainActivity.getEstacion().getLat());
                devolucion.put(Estacion.LON,MainActivity.getEstacion().getLon());
                devolucion.put(Estacion.ESTADO_OPERATIVO,MainActivity.getEstacion().isEstado_operativo());
                //Incorporación del JSON a la conexión
                OutputStreamWriter out_devolucion = new OutputStreamWriter(con_devolucion.getOutputStream());
                out_devolucion.write(devolucion.toString());
                out_devolucion.flush();
                out_devolucion.close();
                //Verificación estado y cierre de conexión
                int status_request_devolucion_estacion = con_devolucion.getResponseCode();
                Log.d("status_req_devolucion_e",Integer.toString(status_request_devolucion_estacion));
                con_devolucion.disconnect();

                //Setup de la conexión
                URL url = new URL(MainActivity.IP + MainActivity.PUERTO + urlDevolucionVcub + idVcub + "/");
                HttpURLConnection con = (HttpURLConnection) url.openConnection();
                con.setDoOutput(true);
                con.setDoInput(true);
                con.setRequestProperty("Authorization", "Token " + Login.auth_token);
                con.setRequestMethod("GET");
                StringBuilder result = new StringBuilder();
                //Lectura del resultado
                if (con.getResponseCode() == 201) {
                    InputStream in = new BufferedInputStream(con.getInputStream());
                    BufferedReader reader = new BufferedReader(new InputStreamReader(in));
                    String line;
                    while ((line = reader.readLine()) != null) {
                        result.append(line);
                    }
                    con.disconnect();
                }
                JSONObject jObject = new JSONObject(result.toString());
                String registro = jObject.getString(Vcub.REGISTRO);
                String marca = jObject.getString(Vcub.MARCA);
                String modelo = jObject.getString(Vcub.MODELO);
                String fecha_fabricacion = jObject.getString(Vcub.FECHA_FABRICACION);
                String estacion = jObject.getString(Vcub.ESTACION);
                boolean en_transito = jObject.getBoolean(Vcub.EN_TRANSITO);
                boolean estado_operativo = jObject.getBoolean(Vcub.ESTADO_OPERATIVO);
                //Instanciación del vcub
                vcub = new Vcub(registro,marca,modelo,fecha_fabricacion,estacion,en_transito,estado_operativo);

                //Setup de la conexión
                URL url_devolucionVcub = new URL(MainActivity.IP + MainActivity.PUERTO + urlDevolucionVcub);
                HttpURLConnection con_devolucionVcub = (HttpURLConnection)url_devolucionVcub.openConnection();
                con_devolucionVcub.setDoOutput(true);
                con_devolucionVcub.setDoInput(true);
                con_devolucionVcub.setRequestProperty("Content-Type", "application/json");
                con_devolucionVcub.setRequestProperty("Accept", "application/json");
                con.setRequestProperty("Authorization", "Token " + Login.auth_token);
                con_devolucionVcub.setRequestMethod("PUT");
                //Setup del JSON
                JSONObject devolucionVcub   = new JSONObject();
                devolucionVcub.put(Vcub.REGISTRO, vcub.getRegistro());
                devolucionVcub.put(Vcub.MARCA,vcub.getMarca());
                devolucionVcub.put(Vcub.MODELO,vcub.getModelo());
                devolucionVcub.put(Vcub.FECHA_FABRICACION,vcub.getFecha_fabricacion());
                devolucionVcub.put(Vcub.ESTACION,vcub.getEstacion());
                devolucionVcub.put(Vcub.EN_TRANSITO,false);
                devolucionVcub.put(Vcub.ESTADO_OPERATIVO,vcub.isEstado_operativo());
                //Incorporación del JSON a la conexión
                OutputStreamWriter out_devolucionVcub = new OutputStreamWriter(con_devolucion.getOutputStream());
                out_devolucionVcub.write(devolucion.toString());
                out_devolucionVcub.flush();
                out_devolucionVcub.close();
                //Verificación estado y cierre de conexión
                int status_request_devolucion_vcub = con_devolucion.getResponseCode();
                Log.d("status_req_devolucion_v",Integer.toString(status_request_devolucion_vcub));
                con_devolucion.disconnect();

                if(status_request_devolucion_estacion > 199 && status_request_devolucion_estacion <300 && status_request_devolucion_vcub > 199 && status_request_devolucion_vcub <300){
                    return "El vcub con id " + vcub.getRegistro() + " ha sido devuelta.";
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
            return "El vcub con id " + vcub.getRegistro() + " no ha sido devuelta con éxito. Por favor intente de nuevo!";
        }

        @Override
        protected void onPostExecute(String result) {
            textView.setText(result);
        }
    }

    private void openSearch() {
        Toast.makeText(this, "Search button pressed", Toast.LENGTH_SHORT).show();
    }

    private void openSettings() {
        Toast.makeText(this, "Settings button pressed", Toast.LENGTH_SHORT).show();
    }
}
