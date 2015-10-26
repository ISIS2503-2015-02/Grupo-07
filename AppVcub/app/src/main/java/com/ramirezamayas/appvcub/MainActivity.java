package com.ramirezamayas.appvcub;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.StrictMode;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.*;
import android.widget.EditText;
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
    public static final String IP = "https://127.0.0.1";

    //puerto host servidor
    public static final String PUERTO = ":9345/";

    //puerto host servidor
    public static final String EXTRA_MESSAGE = "message";

    //URL recuperacion info estacion
    private String urlInfo = "estaciones/";

    //Estacion del app
    private static Estacion estacion;

    //ID estación vcub
    private static String idEstacion;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //Recuperación del ID compartido por Login
        Intent intent = getIntent();
        idEstacion = intent.getStringExtra(Login.USUARIO);
        urlInfo += idEstacion + "/";
        //Recuperación de la info de la estación identificada
        new RecuperarInfoTask().execute();
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

    //Tarea asincrónica para la recuperación de la información del movibus autenticado
    class RecuperarInfoTask extends AsyncTask<Void, Void, String> {

        //Método ejecutable de AsyncTask
        protected String doInBackground(Void... nada) {
            try {
                //Setup de la conexión
                URL url = new URL(MainActivity.IP + MainActivity.PUERTO + urlInfo);
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
                return result.toString();
            } catch (Exception e) {
                Log.d("Error:", "falló recuperación de info de movibus.");
                e.printStackTrace();
                return null;
            }
        }

        protected void onPostExecute(String result) {
            JSONObject jObject = null;
            try {
                //Recuperación de la información del movibus
                jObject = new JSONObject(result);
                String nombre = jObject.getString(Estacion.NOMBRE);
                String fecha_construcion = jObject.getString(Estacion.FECHA_CONSTRUCCION);
                int cap_actual = jObject.getInt(Estacion.CAP_ACTUAL);
                int cap_max = jObject.getInt(Estacion.CAP_MAX);
                int lon = jObject.getInt(Estacion.LON);
                int lat = jObject.getInt(Estacion.LAT);
                boolean estado_operativo = jObject.getBoolean(Estacion.ESTADO_OPERATIVO);
                //Instanciación del movibus
                estacion = new Estacion(nombre, fecha_construcion, cap_actual, cap_max, lon, lat, estado_operativo);
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
    }

    /** Llamado para reportar el prestamo de un Vcub */
    public void reportar_prestamo(View view) {
        Intent intent = new Intent(this, Reportar_prestamo.class);
        EditText editText = (EditText) findViewById(R.id.edit_message_prestamo);
        String message = editText.getText().toString();
        intent.putExtra(EXTRA_MESSAGE, message);
        startActivity(intent);
    }

    /** Llamado para reportar la devolución de un Vcub */
    public void reportar_devolucion(View view) {
        Intent intent = new Intent(this, Reportar_devolucion.class);
        EditText editText = (EditText) findViewById(R.id.edit_message_devolucion);
        String message = editText.getText().toString();
        intent.putExtra(EXTRA_MESSAGE, message);
        startActivity(intent);
    }

    public static Estacion getEstacion() {
        return estacion;
    }

    /** Placeholders de la Action Bar */
    private void openSearch() {
        Toast.makeText(this, "Search button pressed", Toast.LENGTH_SHORT).show();
    }

    private void openSettings() {
        Toast.makeText(this, "Settings button pressed", Toast.LENGTH_SHORT).show();
    }
}
