package com.ramirezamayas.appmovibus;

import android.content.Intent;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.*;
import android.widget.EditText;
import android.widget.Toast;



public class MainActivity extends ActionBarActivity {

    //ip host servidor
    public static final String ip = "127.0.0.1";

    //puerto host servidor
    public static final String puerto = "9345";

    //Identificador movibus
    private static String idMoviBus;

    //Identificador recorrido
    private static int idRecorrido;

    //Identificador recorrido
    private static int idReserva;

    //Detener recorrido?
    private static boolean detenerRecorrido = true;

    //Getters
    public static String darIdMovibus( ){ return idMoviBus; }

    public static int darIdRecorrido( ){ return idRecorrido; }

    public static int darIdReserva( ){ return idReserva; }

    public static boolean darDetenerRecorrido(){ return detenerRecorrido; }

    //Setters
    public static void aumentarIdRecorrido( ){ idRecorrido++; }

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
        setContentView(R.layout.activity_main);
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

