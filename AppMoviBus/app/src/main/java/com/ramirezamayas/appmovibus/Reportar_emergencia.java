package com.ramirezamayas.appmovibus;

import android.os.AsyncTask;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.widget.TextView;
import android.widget.Toast;
import org.json.JSONObject;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;


public class Reportar_emergencia extends ActionBarActivity {

    private TextView textView;

    String urlEmergencia_ = "movibuses/" + MainActivity.getMovibus().getPlaca() + "/";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        //Display del TextView
        textView = new TextView(this);
        textView.setTextSize(30);
        setContentView(textView);
        //Ejecución actividad asincrónica reporte emergencia
        new EnviarReporteEmergencia().execute();

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

    private class EnviarReporteEmergencia extends AsyncTask<Void, Void, String> {
        @Override
        protected String doInBackground(Void... nada) {
            try {
                //Setup de la conexión
                URL urlEmergencia = new URL(MainActivity.IP + MainActivity.PUERTO + urlEmergencia_);
                HttpURLConnection con_emergencia = (HttpURLConnection)urlEmergencia.openConnection();
                con_emergencia.setRequestProperty("Content-Type", "application/json");
                con_emergencia.setRequestProperty("Authorization", "Token " + Login.auth_token);
                con_emergencia.setRequestMethod("PUT");
                //Setup del JSON
                JSONObject movibus = new JSONObject();
                movibus.put(Movibus.PLACA,MainActivity.getMovibus().getPlaca());
                movibus.put(Movibus.MARCA,MainActivity.getMovibus().getMarca());
                movibus.put(Movibus.MODELO,MainActivity.getMovibus().getModelo());
                movibus.put(Movibus.FECHA_FABRICACION,MainActivity.getMovibus().getFecha_fabricacion());
                movibus.put(Movibus.RUTA,MainActivity.getMovibus().getRuta());
                movibus.put(Movibus.CAP_MAX,MainActivity.getMovibus().getCap_max());
                movibus.put(Movibus.ESTADO_OPERATIVO,false);
                movibus.put(Movibus.ULTIMO_RECORRIDO,MainActivity.getMovibus().getUltimo_recorrido());
                movibus.put(Movibus.RESERVA_ACTUAL,MainActivity.getMovibus().getReserva_actual());
                movibus.put(Movibus.CONDUCTOR_ACTUAL,MainActivity.getMovibus().getConductor_actual());
                //Incorporación del JSON a la conexión
                OutputStreamWriter out = new OutputStreamWriter(con_emergencia.getOutputStream());
                out.write(movibus.toString());
                out.flush();
                //Verificación estado y cierre de conexión
                int status_request_emergencia = con_emergencia.getResponseCode();
                Log.d("status_req_emergencia",Integer.toString(status_request_emergencia));
                con_emergencia.disconnect();
                if(status_request_emergencia > 199 && status_request_emergencia <300){
                    return "Se ha notificado sobre la emergencia del movibus con id " + MainActivity.getMovibus().getPlaca() + ". La ayuda viene en camino.";
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
            return "No ha sido posible notificar la emergencia del movibus con id " + MainActivity.getMovibus().getPlaca() + ". Por favor intente de nuevo!";
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
