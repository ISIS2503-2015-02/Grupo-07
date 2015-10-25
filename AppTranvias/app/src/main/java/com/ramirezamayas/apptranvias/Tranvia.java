package com.ramirezamayas.apptranvias;

/**
 * Created by RamirezAmayaS on 10/25/15.
 */
public class Tranvia {

    public final static String PLACA = "placa";

    public final static String MARCA = "marca";

    public final static String MODELO = "modelo";

    public final static String FECHA_FABRICACION = "fecha_fabricacion";

    public final static String CAP_MAX = "cap_max";

    public final static String LINEA = "linea";

    public final static String ESTADO_OPERATIVO = "estado_operativo";

    public final static String ULTIMO_RECORRIDO = "ultimo_recorrido";

    public final static String CONDUCTOR_ACTUAL = "conductor_actual";

    private String placa;

    private String marca;

    private String modelo;

    private String fecha_fabricacion;

    private int cap_max;

    private int linea;

    private boolean estado_operativo;

    private String ultimo_recorrido;

    private String conductor_actual;

    public Tranvia(String placa, String marca, String modelo, String fecha_fabricacion, int cap_max, int linea, boolean estado_operativo, String ultimo_recorrido, String conductor_actual) {
        this.placa = placa;
        this.marca = marca;
        this.modelo = modelo;
        this.fecha_fabricacion = fecha_fabricacion;
        this.cap_max = cap_max;
        this.linea = linea;
        this.estado_operativo = estado_operativo;
        this.ultimo_recorrido = ultimo_recorrido;
        this.conductor_actual = conductor_actual;
    }

    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getFecha_fabricacion() {
        return fecha_fabricacion;
    }

    public void setFecha_fabricacion(String fecha_fabricacion) {
        this.fecha_fabricacion = fecha_fabricacion;
    }

    public int getCap_max() {
        return cap_max;
    }

    public void setCap_max(int cap_max) {
        this.cap_max = cap_max;
    }

    public int getLinea() {
        return linea;
    }

    public void setLinea(int linea) {
        this.linea = linea;
    }

    public boolean isEstado_operativo() {
        return estado_operativo;
    }

    public void setEstado_operativo(boolean estado_operativo) {
        this.estado_operativo = estado_operativo;
    }

    public String getUltimo_recorrido() {
        return ultimo_recorrido;
    }

    public void setUltimo_recorrido(String ultimo_recorrido) {
        this.ultimo_recorrido = ultimo_recorrido;
    }

    public String getConductor_actual() {
        return conductor_actual;
    }

    public void setConductor_actual(String conductor_actual) {
        this.conductor_actual = conductor_actual;
    }
}
