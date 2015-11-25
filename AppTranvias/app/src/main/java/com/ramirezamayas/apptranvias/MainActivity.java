package com.ramirezamayas.apptranvias;

import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;


public class MainActivity extends ActionBarActivity {

    //ip host servidor
    public static final String IP = "http://157.253.158.108";

    //puerto host servidor
    public static final String PUERTO = ":9345/";

    //URL recuperacion info tranvías
    public static String urlInfo = "tranvias/";

    //Tranvía del app
    private static Tranvia tranvia;

    //Identificador tranvía
    private static String idTranvia;

    //Detener recorrido?
    private static boolean detenerRecorrido = true;

    private static boolean first = true;

    //Getters
    public static boolean darDetenerRecorrido(){ return detenerRecorrido; }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        if(first){
            first = false;
            //Recuperación del ID compartido por Login
            Intent intent = getIntent();
            idTranvia = intent.getStringExtra(Login.USUARIO);
            urlInfo += idTranvia + "/";
            //Recuperación de la info del tranvia identificado
            new RecuperarInfoTask().execute();
        }
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

    //Tarea asincrónica para la recuperación de la información del tranvía autenticado
    class RecuperarInfoTask extends AsyncTask<Void, Void, String> {

        //Método ejecutable de AsyncTask
        protected String doInBackground(Void... nada) {
            try {
                //Setup de la conexión
                URL url = new URL(MainActivity.IP + MainActivity.PUERTO + urlInfo);
                HttpURLConnection con = (HttpURLConnection)url.openConnection();
                con.setRequestProperty("Content-Type", "application/json");
                con.setRequestProperty("Authorization", "Token " + Login.auth_token);
                con.setRequestMethod("GET");
                StringBuilder result = new StringBuilder();
                //Lectura del resultado
                if(con.getResponseCode()==200){
                    InputStream in = new BufferedInputStream(con.getInputStream());
                    BufferedReader reader = new BufferedReader(new InputStreamReader(in));
                    String line;
                    while ((line = reader.readLine()) != null) {
                        result.append(line);
                    }
                    con.disconnect();
                }
                return result.toString();
            } catch (Exception e) {
                Log.d("Error:", "falló recuperación de info de tranvía.");
                e.printStackTrace();
                return null;
            }
        }

        protected void onPostExecute(String result) {
            JSONObject jObject = null;
            try {
                //Recuperación de la información del tranvia
                jObject = new JSONObject(result);
                String placa = jObject.getString(Tranvia.PLACA);
                String marca = jObject.getString(Tranvia.MARCA);
                String modelo = jObject.getString(Tranvia.MODELO);
                String fecha_fabricacion = jObject.getString(Tranvia.FECHA_FABRICACION);
                int cap_max = jObject.getInt(Tranvia.CAP_MAX);
                int linea = jObject.getInt(Tranvia.LINEA);
                boolean estado_operativo = jObject.getBoolean(Tranvia.ESTADO_OPERATIVO);
                String ultimo_recorrido = "0";
                String conductor_actual = "1";
                //Instanciación del movibus
                tranvia = new Tranvia(placa,marca,modelo,fecha_fabricacion,cap_max,linea,estado_operativo,ultimo_recorrido,conductor_actual);
                Log.d("conductor_tranvia",tranvia.getConductor_actual());
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
    }

    public static Tranvia getTranvia() {
        return tranvia;
    }

    //Inicia actividad Iniciar_recorrido
    public void iniciar_recorrido(View view) {
        detenerRecorrido = true;
        Intent intent = new Intent(this, Iniciar_recorrido.class);
        startActivity(intent);
    }

    //Inicia actividad Reportar_emergencia
    public void reportar_emergencia(View view) {
        Intent intent = new Intent(this, Reportar_emergencia.class);
        startActivity(intent);
    }

    //Detiene la actividad Iniciar_recorrido
    public void detener_recorrido(View view) {
        detenerRecorrido = false;
        int recorridoActual = Integer.parseInt(tranvia.getUltimo_recorrido());
        tranvia.setUltimo_recorrido(Integer.toString(recorridoActual + 1));
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