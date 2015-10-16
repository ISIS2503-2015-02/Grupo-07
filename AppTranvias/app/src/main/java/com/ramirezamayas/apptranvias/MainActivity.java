package com.ramirezamayas.apptranvias;

import android.content.Intent;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Toast;


public class MainActivity extends ActionBarActivity {

    /** Id tranvia */
    private static String idTranvia = "1";

    /** Id proximo recorrido */
    private static int idRecorrido = 1;

    /** Detener recorrido */
    private static boolean detenerRecorrido = true;

    /** Getters and setters */
    public static String darIdTranvia( ){ return idTranvia; }

    public static int darIdRecorrido( ){ return idRecorrido; }

    public static boolean darDetenerRecorrido(){ return detenerRecorrido; }

    public static void aumentarIdRecorrido( ){ idRecorrido++; }

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

    public void iniciar_recorrido(View view) {
        detenerRecorrido = true;
        Intent intent = new Intent(this, Iniciar_recorrido.class);
        startActivity(intent);
    }

    public void reportar_emergencia(View view) {
        Intent intent = new Intent(this, Reportar_emergencia.class);
        startActivity(intent);
    }

    public void detener_recorrido(View view) {
        detenerRecorrido = false;
    }

    private void openSearch() {
        Toast.makeText(this, "Search button pressed", Toast.LENGTH_SHORT).show();
    }

    private void openSettings() {
        Toast.makeText(this, "Settings button pressed", Toast.LENGTH_SHORT).show();
    }
}
