package com.ramirezamayas.appvcub;

import android.content.Intent;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.*;
import android.widget.EditText;
import android.widget.Toast;


public class MainActivity extends ActionBarActivity {

    /** Mensaje enviado entre actividades */
    public final static String EXTRA_MESSAGE = "com.ramirezamayas.appmovibus.MESSAGE";

    /** Número de Vcubs disponibles */
    private static int vcubs = 20;


    /** Getters and setters */
    public static int darVcubs (){
        return vcubs;
    }

    public static void aumentarVcubs(int n){
        vcubs += n;
    }

    public static void disminuirVcubs(int n){
        vcubs -= n;
    }

    /** Métodos ciclo de vida app */
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
        Intent intent = new Intent(this, Reportar_prestamo.class);
        EditText editText = (EditText) findViewById(R.id.edit_message_devolucion);
        String message = editText.getText().toString();
        intent.putExtra(EXTRA_MESSAGE, message);
        startActivity(intent);
    }

    /** Placeholders de la Action Bar */
    private void openSearch() {
        Toast.makeText(this, "Search button pressed", Toast.LENGTH_SHORT).show();
    }

    private void openSettings() {
        Toast.makeText(this, "Settings button pressed", Toast.LENGTH_SHORT).show();
    }
}
