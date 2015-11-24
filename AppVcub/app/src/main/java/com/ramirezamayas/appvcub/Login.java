package com.ramirezamayas.appvcub;

import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONObject;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;


public class Login extends ActionBarActivity {

    public final static String USUARIO = "usuario";

    public final static String CONTRASENA = "contrasena";

    String urlLogin_ = "api-token-auth/";

    public static String auth_token;

    String messageUsuario;

    String messageContrasena;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
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

    public void login(View view){
        //Recuperación texto campo usuario
        EditText editUsuario = (EditText) findViewById(R.id.edit_usuario);
        messageUsuario = editUsuario.getText().toString();
        //Recuperación texto campo contrasena
        EditText editContrasena = (EditText) findViewById(R.id.edit_contrasena);
        messageContrasena = editContrasena.getText().toString();
        //Autenticación usuario
        new LoginTask().execute(messageUsuario, messageContrasena);
    }

    //Tarea de autenticación del usuario
    class LoginTask extends AsyncTask<String, Void, Integer> {

        //Método ejecutable de AsyncTask
        protected Integer doInBackground(String... credenciales) {
            try {
                //Setup de la conexión
                URL urlLogin = new URL(MainActivity.IP + MainActivity.PUERTO + urlLogin_);
                HttpURLConnection con_login = (HttpURLConnection)urlLogin.openConnection();
                con_login.setDoOutput(true);
                con_login.setDoInput(true);
                con_login.setRequestProperty("Content-Type", "application/json");
                con_login.setRequestProperty("Accept", "application/json");
                con_login.setRequestMethod("POST");
                //Setup del JSON
                JSONObject cred   = new JSONObject();
                cred.put("username",credenciales[0]);
                cred.put("password",credenciales[1]);
                //Incorporación del JSON a la conexión
                OutputStreamWriter out = new OutputStreamWriter(con_login.getOutputStream());
                out.write(cred.toString());
                out.flush();
                //Lectura del resultado
                int status_request_login = con_login.getResponseCode();
                Log.d("status_request_login",Integer.toString(status_request_login));
                StringBuilder result = new StringBuilder();
                if(con_login.getResponseCode()==200){
                    InputStream in = new BufferedInputStream(con_login.getInputStream());
                    BufferedReader reader = new BufferedReader(new InputStreamReader(in));
                    String line;
                    while ((line = reader.readLine()) != null) {
                        result.append(line);
                    }
                }
                JSONObject jObject = new JSONObject(result.toString());
                auth_token = jObject.getString("token");
                con_login.disconnect();
                return status_request_login;
            } catch (Exception e) {
                Log.d("Error:","falló autenticación de usuario.");
                e.printStackTrace();
                return null;
            }
        }

        protected void onPostExecute(int responseCode) {
            if(responseCode==200){
                iniciarMainActivity();
            }
            else{
                notificarError();
            }
        }
    }

    public void iniciarMainActivity(){
        //Inicio actividad principal
        Intent intent = new Intent(this, MainActivity.class);
        intent.putExtra(USUARIO,messageUsuario);
        intent.putExtra(CONTRASENA,messageUsuario);
        startActivity(intent);
    }

    public void notificarError() {
        Toast.makeText(this, "Credenciales equivocadas", Toast.LENGTH_SHORT).show();
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
