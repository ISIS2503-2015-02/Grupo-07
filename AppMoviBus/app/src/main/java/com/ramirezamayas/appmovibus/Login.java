package com.ramirezamayas.appmovibus;

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

import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;


public class Login extends ActionBarActivity {

    String urlLogin = "login/";

    public void login(View view){
        //Recuperación texto campo usuario
        EditText editUsuario = (EditText) findViewById(R.id.edit_usuario);
        String messageUsuario = editUsuario.getText().toString();
        //Recuperación texto campo contrasena
        EditText editContrasena = (EditText) findViewById(R.id.edit_contrasena);
        String messageContrasena = editContrasena.getText().toString();
        //Autenticación usuario
        new LoginTask().execute(messageUsuario, messageContrasena);
    }

    class LoginTask extends AsyncTask<String, Void, Integer> {

        protected Integer doInBackground(String... credenciales) {
            try {
                //Setup de la conexión
                URL url = new URL(MainActivity.IP + MainActivity.PUERTO + urlLogin);
                HttpURLConnection con = (HttpURLConnection)url.openConnection();
                con.setDoOutput(true);
                con.setDoInput(true);
                con.setRequestProperty("Content-Type", "application/json");
                con.setRequestProperty("Accept", "application/json");
                con.setRequestMethod("POST");
                //Setup del JSON
                JSONObject cred   = new JSONObject();
                cred.put("username",credenciales[0]);
                cred.put("password",credenciales[1]);
                //Incorporación del JSON a la conexión
                OutputStreamWriter out = new OutputStreamWriter(con.getOutputStream());
                out.write(cred.toString());
                out.flush();
                //Lectura del resultado
                int result = con.getResponseCode();
                return result;
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
}
