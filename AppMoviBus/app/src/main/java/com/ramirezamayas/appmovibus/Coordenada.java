package com.ramirezamayas.appmovibus;

/**
 * Created by RamirezAmayaS on 10/23/15.
 */
public class Coordenada {

    private String latitud;

    private String longitud;

    private String movibus;

    private String recorrido;

    public Coordenada(String latitud, String longitud, String movibus, String recorrido) {
        this.latitud = latitud;
        this.longitud = longitud;
        this.movibus = movibus;
        this.recorrido = recorrido;
    }

    public String getLatitud() {
        return latitud;
    }

    public void setLatitud(String latitud) {
        this.latitud = latitud;
    }

    public String getLongitud() {
        return longitud;
    }

    public void setLongitud(String longitud) {
        this.longitud = longitud;
    }

    public String getMovibus() {
        return movibus;
    }

    public void setMovibus(String movibus) {
        this.movibus = movibus;
    }

    public String getRecorrido() {
        return recorrido;
    }

    public void setRecorrido(String recorrido) {
        this.recorrido = recorrido;
    }
}
