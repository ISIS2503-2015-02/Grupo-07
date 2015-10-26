package com.ramirezamayas.appvcub;

/**
 * Created by RamirezAmayaS on 10/25/15.
 */
public class Estacion {

    public static final String NOMBRE = "nombre";

    public static final String FECHA_CONSTRUCCION = "fecha_construccion";

    public static final String CAP_ACTUAL = "cap_actual";

    public static final String CAP_MAX = "cap_max";

    public static final String LON = "lon";

    public static final String LAT = "lat";

    public static final String ESTADO_OPERATIVO = "estado_operativo";

    private String nombre;

    private String fecha_construccion;

    private int cap_actual;

    private int cap_max;

    private int lon;

    private int lat;

    private boolean estado_operativo;

    public Estacion(String nombre, String fecha_construccion, int cap_actual, int cap_max, int lon, int lat, boolean estado_operativo) {
        this.nombre = nombre;
        this.fecha_construccion = fecha_construccion;
        this.cap_actual = cap_actual;
        this.cap_max = cap_max;
        this.lon = lon;
        this.lat = lat;
        this.estado_operativo = estado_operativo;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getFecha_construccion() {
        return fecha_construccion;
    }

    public void setFecha_construccion(String fecha_construccion) {
        this.fecha_construccion = fecha_construccion;
    }

    public int getCap_actual() {
        return cap_actual;
    }

    public void setCap_actual(int cap_actual) {
        this.cap_actual = cap_actual;
    }

    public int getCap_max() {
        return cap_max;
    }

    public void setCap_max(int cap_max) {
        this.cap_max = cap_max;
    }

    public int getLon() {
        return lon;
    }

    public void setLon(int lon) {
        this.lon = lon;
    }

    public int getLat() {
        return lat;
    }

    public void setLat(int lat) {
        this.lat = lat;
    }

    public boolean isEstado_operativo() {
        return estado_operativo;
    }

    public void setEstado_operativo(boolean estado_operativo) {
        this.estado_operativo = estado_operativo;
    }
}
