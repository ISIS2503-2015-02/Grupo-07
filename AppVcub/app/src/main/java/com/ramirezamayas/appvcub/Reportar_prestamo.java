package com.ramirezamayas.appvcub;

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


public class Reportar_prestamo extends ActionBarActivity {

    private TextView textView;

    //URL recuperacion info estacion
    private String urlPrestamoEstacion = "estaciones/";

    //URL recuperacion info vcub
    private String urlPrestamoVcub = "vcub/";

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
        MainActivity.getEstacion().setCap_actual(MainActivity.getEstacion().getCap_actual() - 1);
        new EnviarReportePrestamo().execute(idVcub);
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

    private class EnviarReportePrestamo extends AsyncTask<String, Void, String> {
        @Override
        protected String doInBackground(String... message) {
            try {
                //Setup de la conexión
                URL url_prestamo = new URL(MainActivity.IP + MainActivity.PUERTO + urlPrestamoEstacion);
                HttpURLConnection con_prestamo = (HttpURLConnection)url_prestamo.openConnection();
                con_prestamo.setDoOutput(true);
                con_prestamo.setDoInput(true);
                con_prestamo.setRequestProperty("Content-Type", "application/json");
                con_prestamo.setRequestProperty("Accept", "application/json");
                con_prestamo.setRequestMethod("PUT");
                //Setup del JSON
                JSONObject prestamo   = new JSONObject();
                prestamo.put(Estacion.NOMBRE, MainActivity.getEstacion().getNombre());
                prestamo.put(Estacion.FECHA_CONSTRUCCION,MainActivity.getEstacion().getFecha_construccion());
                prestamo.put(Estacion.CAP_ACTUAL,MainActivity.getEstacion().getCap_actual());
                prestamo.put(Estacion.CAP_MAX,MainActivity.getEstacion().getCap_max());
                prestamo.put(Estacion.LAT,MainActivity.getEstacion().getLat());
                prestamo.put(Estacion.LON,MainActivity.getEstacion().getLon());
                prestamo.put(Estacion.ESTADO_OPERATIVO,MainActivity.getEstacion().isEstado_operativo());
                //Incorporación del JSON a la conexión
                OutputStreamWriter out_prestamo = new OutputStreamWriter(con_prestamo.getOutputStream());
                out_prestamo.write(prestamo.toString());
                out_prestamo.flush();
                out_prestamo.close();
                //Verificación estado y cierre de conexión
                int status_request_prestamo_estacion = con_prestamo.getResponseCode();
                Log.d("status_req_prestamo_e",Integer.toString(status_request_prestamo_estacion));
                con_prestamo.disconnect();

                //Setup de la conexión
                URL url = new URL(MainActivity.IP + MainActivity.PUERTO + urlPrestamoVcub + idVcub + "/");
                HttpURLConnection con = (HttpURLConnection) url.openConnection();
                con.setDoOutput(true);
                con.setDoInput(true);
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
                URL url_prestamoVcub = new URL(MainActivity.IP + MainActivity.PUERTO + urlPrestamoVcub);
                HttpURLConnection con_prestamoVcub = (HttpURLConnection)url_prestamoVcub.openConnection();
                con_prestamoVcub.setDoOutput(true);
                con_prestamoVcub.setDoInput(true);
                con_prestamoVcub.setRequestProperty("Content-Type", "application/json");
                con_prestamoVcub.setRequestProperty("Accept", "application/json");
                con_prestamoVcub.setRequestMethod("PUT");
                //Setup del JSON
                JSONObject prestamoVcub   = new JSONObject();
                prestamoVcub.put(Vcub.REGISTRO, vcub.getRegistro());
                prestamoVcub.put(Vcub.MARCA,vcub.getMarca());
                prestamoVcub.put(Vcub.MODELO,vcub.getModelo());
                prestamoVcub.put(Vcub.FECHA_FABRICACION,vcub.getFecha_fabricacion());
                prestamoVcub.put(Vcub.ESTACION,vcub.getEstacion());
                prestamoVcub.put(Vcub.EN_TRANSITO,true);
                prestamoVcub.put(Vcub.ESTADO_OPERATIVO,vcub.isEstado_operativo());
                //Incorporación del JSON a la conexión
                OutputStreamWriter out_prestamoVcub = new OutputStreamWriter(con_prestamo.getOutputStream());
                out_prestamoVcub.write(prestamo.toString());
                out_prestamoVcub.flush();
                out_prestamoVcub.close();
                //Verificación estado y cierre de conexión
                int status_request_prestamo_vcub = con_prestamo.getResponseCode();
                Log.d("status_req_prestamo_v",Integer.toString(status_request_prestamo_vcub));
                con_prestamo.disconnect();

                if(status_request_prestamo_estacion > 199 && status_request_prestamo_estacion <300 && status_request_prestamo_vcub > 199 && status_request_prestamo_vcub <300){
                    return "El vcub con id " + vcub.getRegistro() + " ha sido prestada.";
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
            return "El vcub con id " + vcub.getRegistro() + " no ha sido prestada con éxito. Por favor intente de nuevo!";
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
