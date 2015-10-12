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

import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;


public class Reportar_devolucion extends ActionBarActivity {

    private TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        Intent intent = getIntent();
        String message = intent.getStringExtra(MainActivity.EXTRA_MESSAGE);

        textView = new TextView(this);
        textView.setTextSize(30);
        MainActivity.disminuirCapacidad(1);
        new EnviarReporteDevolucion().execute(message);

        setContentView(textView);
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

    private class EnviarReporteDevolucion extends AsyncTask<String, Void, String> {
        @Override
        protected String doInBackground(String... message) {
            try {
                HttpClient client = new DefaultHttpClient();
                HttpConnectionParams.setConnectionTimeout(client.getParams(), 1000);
                HttpResponse response;
                JSONObject json_estacion = new JSONObject();
                JSONObject json_vcub = new JSONObject();

                HttpPut put_estacion = new HttpPut("http://186.80.206.189:9347/estaciones/" + MainActivity.darIdEstacion() + "/");
                json_estacion.put("nombre", 1);
                json_estacion.put("fecha_construccion", "2015-01-01");
                json_estacion.put("cap_actual", MainActivity.darCapacidad());
                json_estacion.put("cap_max", 20);
                json_estacion.put("lon", 1.0);
                json_estacion.put("lat", 1.0);
                json_estacion.put("vcub","[]");
                StringEntity se_estacion = new StringEntity( json_estacion.toString());
                se_estacion.setContentType(new BasicHeader(HTTP.CONTENT_TYPE, "application/json"));
                put_estacion.setEntity(se_estacion);
                response = client.execute(put_estacion);

                if(response!=null){
                    InputStream in = response.getEntity().getContent();
                }
                int d1 = response.getStatusLine().getStatusCode();
                Log.d("Status", String.valueOf(d1));

                HttpPut put_vcub = new HttpPut("http://186.80.206.189:9347/vcubs/" + Integer.parseInt(message[0]) + "/");
                json_vcub.put("registro", "1");
                json_vcub.put("marca", "1");
                json_vcub.put("modelo", "1");
                json_estacion.put("fecha_construccion", "2015-01-01");
                json_vcub.put("estacion", MainActivity.darIdEstacion());
                json_vcub.put("en_transito", false);
                json_vcub.put("estado_operativo", true);
                StringEntity se_vcub = new StringEntity( json_vcub.toString());
                se_vcub.setContentType(new BasicHeader(HTTP.CONTENT_TYPE, "application/json"));
                put_vcub.setEntity(se_vcub);
                response = client.execute(put_vcub);

                if(response!=null){
                    InputStream in = response.getEntity().getContent();
                }
                int d2 = response.getStatusLine().getStatusCode();
                Log.d("Status", String.valueOf(d2));

                if(d1 > 199 && d1 <300 && d2 > 199 && d2 <300){
                    return "El vcub con id " + message[0] + " ha sido devuelta.";
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
            MainActivity.aumentarCapacidad(1);
            return "El vcub con id " + message[0] + " no ha sido devuelta con éxito. Por favor intente de nuevo!";
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
