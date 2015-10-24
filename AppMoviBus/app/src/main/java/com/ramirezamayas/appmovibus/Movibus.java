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

    private String placa;

    private String marca;

    private String modelo;

    private String fecha_fabricacion;

    private String ruta;

    private int cap_max;

    private boolean estado_operativo;

    public Movibus(String placa, String marca, String modelo, String fecha_fabricacion, String ruta, int cap_max, boolean estado_operativo) {
        this.placa = placa;
        this.marca = marca;
        this.modelo = modelo;
        this.fecha_fabricacion = fecha_fabricacion;
        this.ruta = ruta;
        this.cap_max = cap_max;
        this.estado_operativo = estado_operativo;
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


}
