package com.ramirezamayas.appMoviBus;

import android.os.StrictMode;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;

import com.ramirezamayas.appMoviBus.R;

import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;


public class SendTCPActivity extends ActionBarActivity {

    GPSTracker gpsTracker;

    TextView textViewLat;
    TextView textViewLon;
    TextView textViewAlt;
    TextView textViewVel;

    private String serverMessage;
    private String serverIP;
    private int serverPortTCP;
    PrintWriter out;

    boolean detener;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_enviar_tcp);

        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);

        serverIP = "10.0.2.2";
        serverPortTCP = 9345;

        try{
            //InetAddress serverAddress = InetAddress.getByName(serverIP);
            //final Socket socket = new Socket(serverAddress,serverPortTCP);
            //out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(socket.getOutputStream())), true);

            textViewLat = (TextView)findViewById(R.id.texto_lat);
            textViewLon = (TextView)findViewById(R.id.texto_lon);
            textViewAlt = (TextView)findViewById(R.id.texto_alt);
            textViewVel = (TextView)findViewById(R.id.texto_vel);

            detener = false;

            Thread t = new Thread() {

                @Override
                public void run() {
                    try {
                        //out.println("Hello\r");
                        while (!detener) {
                            Thread.sleep(1);
                            runOnUiThread(new Runnable() {
                                @Override
                                public void run() {
                                    nuevoTracker();

                                    try{
                                        InetAddress serverAddress = InetAddress.getByName(serverIP);
                                        final Socket socket = new Socket(serverAddress,serverPortTCP);
                                        out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(socket.getOutputStream())), true);

                                        serverMessage = "INFO;";

                                        textViewLat.setText("Latitud: ");
                                        textViewLat.append(String.format("%.2f",gpsTracker.getLatitude()));
                                        serverMessage += (String.format("%.2f",gpsTracker.getLatitude())+";");

                                        textViewLon.setText("Longitud: ");
                                        textViewLon.append(String.format("%.2f",gpsTracker.getLongitude()));
                                        serverMessage += (String.format("%.2f",gpsTracker.getLongitude())+";");

                                        textViewAlt.setText("Altitud: ");
                                        textViewAlt.append(String.format("%.2f",gpsTracker.getAltitude()));
                                        serverMessage += (String.format("%.2f",gpsTracker.getAltitude())+";");

                                        textViewVel.setText("Velocidad: ");
                                        textViewVel.append(String.format("%.2f", gpsTracker.getSpeed()));
                                        serverMessage += (String.format("%.2f",gpsTracker.getSpeed()));

                                        Log.d("prueba",serverMessage);

                                        out.println(serverMessage);

                                        out.close();

                                        socket.close();
                                    }
                                    catch(Exception e){
                                        e.printStackTrace();
                                    }
                                }
                            });
                        }
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            };

            t.start();
        }
        catch(Exception e){
            e.printStackTrace();
        }
    }

    private void nuevoTracker() {
        gpsTracker = new GPSTracker(this);
    }

    public void detener(View view){
        detener=true;
        try{
            InetAddress serverAddress = InetAddress.getByName(serverIP);
            final Socket socket = new Socket(serverAddress,serverPortTCP);
            out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(socket.getOutputStream())), true);
            serverMessage = "PRINT";
            out.println(serverMessage);
            out.close();
            socket.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

}
