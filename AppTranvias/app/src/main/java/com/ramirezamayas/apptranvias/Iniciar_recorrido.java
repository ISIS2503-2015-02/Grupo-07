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


public class Iniciar_recorrido extends ActionBarActivity {

    private TextView textView;

    private GPSTracker gpsTracker;

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
        new EnviarReportePosicion().execute();
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

    private class EnviarReportePosicion extends AsyncTask<Void, String, Void> {
        @Override
        protected Void doInBackground(Void...param ) {
            try {
                HttpClient client = new DefaultHttpClient();
                HttpConnectionParams.setConnectionTimeout(client.getParams(), 1000);
                HttpResponse response;
                JSONObject json_recorrido = new JSONObject();
                JSONObject json_posicion = new JSONObject();

                HttpPut put_recorrido = new HttpPut("http://186.80.206.189:9347/recorridoMovibus/");
                json_recorrido.put("inicio", "2015-01-01");
                json_recorrido.put("fin", "2015-01-01");
                json_recorrido.put("tranvia", MainActivity.darIdTranvia());
                json_recorrido.put("linea", "1");
                json_recorrido.put("conductor", "1");
                StringEntity se_estacion = new StringEntity( json_posicion.toString());
                se_estacion.setContentType(new BasicHeader(HTTP.CONTENT_TYPE, "application/json"));
                put_recorrido.setEntity(se_estacion);
                response = client.execute(put_recorrido);
                if(response!=null){
                    InputStream in = response.getEntity().getContent();
                }
                int d2 = response.getStatusLine().getStatusCode();
                Log.d("Status", String.valueOf(d2));

                while (MainActivity.darDetenerRecorrido()){

                    double lat = gpsTracker.getLatitude();
                    double lon = gpsTracker.getLongitude();

                    HttpPut put_posicion = new HttpPut("http://186.80.206.189:9347/coordenadasMovibus/");
                    json_posicion.put("latitud", lat);
                    json_posicion.put("longitud", lon);
                    json_posicion.put("movibus", MainActivity.darIdTranvia());
                    json_posicion.put("recorrido", MainActivity.darIdRecorrido());
                    StringEntity se_posicion = new StringEntity( json_posicion.toString());
                    se_estacion.setContentType(new BasicHeader(HTTP.CONTENT_TYPE, "application/json"));
                    put_posicion.setEntity(se_estacion);
                    response = client.execute(put_posicion);
                    if(response!=null){
                        InputStream in = response.getEntity().getContent();
                    }
                    int d1 = response.getStatusLine().getStatusCode();
                    Log.d("Status", String.valueOf(d1));

                    if(d1 > 199 && d1 <300 && d1 > 199 && d1 <300){
                        publishProgress("Reportando posicion (lat = " + lat + ", lon = " + lon + ")");
                        MainActivity.aumentarIdRecorrido();
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
        protected void onProgressUpdate(String... params) {
            textView.setText(params[0]);
        }
    }

    private void openSearch() {
        Toast.makeText(this, "Search button pressed", Toast.LENGTH_SHORT).show();
    }

    private void openSettings() {
        Toast.makeText(this, "Settings button pressed", Toast.LENGTH_SHORT).show();
    }
}
