package gettingstarted.getttngstarted;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;

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
import java.util.ArrayList;

public class MyActivity extends AppCompatActivity {

    public final static String EXTRA_MESSAGE = "gettingstarted.getttngstarted.MESSAGE";

    public final static String IP = "http://186.80.206.189:9347/";
    public final static String URI = "reservasUsuario";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_my);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_my, menu);
        return true;
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
    public String procesar(String fecha,int usuario, String fehcaPorgramada, ArrayList<Integer> recorrido )
    {
        try {
            HttpClient client = new DefaultHttpClient();
            HttpConnectionParams.setConnectionTimeout(client.getParams(), 1000);
            HttpResponse response;
            JSONObject json_estacion = new JSONObject();
            JSONObject json_vcub = new JSONObject();

            HttpPut put_solictud = new HttpPut(IP +URI+ "/");

            json_estacion.put("fecha",fecha);
            json_estacion.put("usuario", usuario);
            json_estacion.put("fecha_programada",fehcaPorgramada);
            json_estacion.put("recorrido",recorrido );

            StringEntity se_estacion = new StringEntity( json_estacion.toString());
            se_estacion.setContentType(new BasicHeader(HTTP.CONTENT_TYPE, "application/json"));
            put_solictud.setEntity(se_estacion);
            response = client.execute(put_solictud);

            if(response!=null){
                InputStream in = response.getEntity().getContent();
            }
            int d = response.getStatusLine().getStatusCode();
            Log.d("Status", String.valueOf(d));

            if(d > 199 && d <300){
                return "Su solicitud de reserva de mobibus para el + " +fehcaPorgramada.toString()  + " esta siendo procesada ";
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return "Lo sentimos, su solicitud no ha sido procesada. Por favor intente de nuevo ";


    }
    public void enviarPeticion(View view)
    {
        Intent intent = new Intent(this, DisplayMessageActivity.class);
        EditText editText = (EditText) findViewById(R.id.email);
        String email = editText.getText().toString();
        editText = (EditText) findViewById(R.id.nombre);
        String nombre = editText.getText().toString();

        editText = (EditText) findViewById(R.id.cedula);
        int cedula = Integer.parseInt(editText.getText().toString());

        editText = (EditText) findViewById(R.id.fecha);
        String fechaReserva=editText.getText().toString();

        editText = (EditText) findViewById(R.id.hora);
        String horaReserva=editText.getText().toString();

        intent.putExtra(EXTRA_MESSAGE, fechaReserva+ "La hora es "+horaReserva );
        startActivity(intent);

    }

}
