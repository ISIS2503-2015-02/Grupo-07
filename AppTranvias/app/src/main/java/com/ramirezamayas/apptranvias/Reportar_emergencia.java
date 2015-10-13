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
import org.apache.http.client.methods.HttpPut;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicHeader;
import org.apache.http.params.HttpConnectionParams;
import org.apache.http.protocol.HTTP;
import org.json.JSONObject;

import java.io.InputStream;


public class Reportar_emergencia extends ActionBarActivity {

    private TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        Intent intent = getIntent();

        textView = new TextView(this);
        textView.setTextSize(30);
        new EnviarReporteEmergencia().execute();

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

    private class EnviarReporteEmergencia extends AsyncTask<String, Void, String> {
        @Override
        protected String doInBackground(String... message) {
            try {
                HttpClient client = new DefaultHttpClient();
                HttpConnectionParams.setConnectionTimeout(client.getParams(), 1000);
                HttpResponse response;
                JSONObject json_estacion = new JSONObject();
                JSONObject json_vcub = new JSONObject();

                HttpPut put_estacion = new HttpPut("http://186.80.206.189:9347/MoviBus/" + MainActivity.darIdTranvia() + "/");
                json_estacion.put("placa", "BOI587");
                json_estacion.put("marca", "Chevrolet");
                json_estacion.put("modelo", "1998");
                json_estacion.put("velocidad_promedio", 10.0);
                json_estacion.put("kilometraje", 1000);
                json_estacion.put("fecha_fabricacion", "2015-01-01");
                json_estacion.put("cap_max",50);
                json_estacion.put("linea",1);
                json_estacion.put("estado_operativo",false);
                StringEntity se_estacion = new StringEntity( json_estacion.toString());
                se_estacion.setContentType(new BasicHeader(HTTP.CONTENT_TYPE, "application/json"));
                put_estacion.setEntity(se_estacion);
                response = client.execute(put_estacion);

                if(response!=null){
                    InputStream in = response.getEntity().getContent();
                }
                int d = response.getStatusLine().getStatusCode();
                Log.d("Status", String.valueOf(d));

                if(d > 199 && d <300){
                    return "Se ha notificado sobre la emergencia del movibus con id + " + MainActivity.darIdTranvia() + ". La ayuda viene en camino.";
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
            return "No ha sido posible notificar la emergencia del movibus con id " + MainActivity.darIdTranvia() + ". Por favor intente de nuevo!";
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
