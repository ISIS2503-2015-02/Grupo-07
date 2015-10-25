package com.ramirezamayas.appmovibus;

import java.util.Date;

/**
 * Created by RamirezAmayaS on 10/23/15.
 */
public class Movibus {

    public final static String PLACA = "placa";

    public final static String MARCA = "marca";

    public final static String MODELO = "modelo";

    public final static String FECHA_FABRICACION = "fecha_fabricacion";

    public final static String RUTA = "ruta";

    public final static String CAP_MAX = "cap_max";

    public final static String ESTADO_OPERATIVO = "estado_operativo";

    public final static String ULTIMO_RECORRIDO = "ultimo_recorrido";

    public final static String RESERVA_ACTUAL = "reserva_actual";

    public final static String CONDUCTOR_ACTUAL = "conductor_actual";

    private String placa;

    private String marca;

    private String modelo;

    private String fecha_fabricacion;

    private String ruta;

    private int cap_max;

    private boolean estado_operativo;

    private String ultimo_recorrido;

    private String reserva_actual;

    private String conductor_actual;

    public Movibus(String placa, String marca, String modelo, String fecha_fabricacion, String ruta, int cap_max, boolean estado_operativo, String ultimo_recorrido, String reserva_actual, String conductor_actual) {
        this.placa = placa;
        this.marca = marca;
        this.modelo = modelo;
        this.fecha_fabricacion = fecha_fabricacion;
        this.ruta = ruta;
        this.cap_max = cap_max;
        this.estado_operativo = estado_operativo;
        this.ultimo_recorrido = ultimo_recorrido;
        this.reserva_actual = reserva_actual;
        this.conductor_actual = conductor_actual;
    }

    public String getPlaca() {
        return placa;
    }

    public String getMarca() {
        return marca;
    }

    public String getModelo() {
        return modelo;
    }

    public String getFecha_fabricacion() {
        return fecha_fabricacion;
    }

    public String getRuta() {
        return ruta;
    }

    public int getCap_max() {
        return cap_max;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public void setFecha_fabricacion(String fecha_fabricacion) {
        this.fecha_fabricacion = fecha_fabricacion;
    }

    public void setRuta(String ruta) {
        this.ruta = ruta;
    }

    public void setCap_max(int cap_max) {
        this.cap_max = cap_max;
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

    public String getReserva_actual() {
        return reserva_actual;
    }

    public void setReserva_actual(String reserva_actual) {
        this.reserva_actual = reserva_actual;
    }

    public String getConductor_actual() {
        return conductor_actual;
    }

    public void setConductor_actual(String conductor_actual) {
        this.conductor_actual = conductor_actual;
    }
}
