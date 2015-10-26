package com.ramirezamayas.appvcub;

/**
 * Created by RamirezAmayaS on 10/25/15.
 */
public class Vcub {

    public static final String REGISTRO = "registro";

    public static final String MARCA = "marca";

    public static final String MODELO = "modelo";

    public static final String FECHA_FABRICACION = "fecha_fabricacion";

    public static final String ESTACION = "estacion";

    public static final String EN_TRANSITO = "en_transito";

    public static final String ESTADO_OPERATIVO = "estado_operativo";

    private String registro;

    private String marca;

    private String modelo;

    private String fecha_fabricacion;

    private String estacion;

    private boolean en_transito;

    private boolean estado_operativo;

    public Vcub(String registro, String marca, String modelo, String fecha_fabricacion, String estacion, boolean en_transito, boolean estado_operativo) {
        this.registro = registro;
        this.marca = marca;
        this.modelo = modelo;
        this.fecha_fabricacion = fecha_fabricacion;
        this.estacion = estacion;
        this.en_transito = en_transito;
        this.estado_operativo = estado_operativo;
    }

    public String getRegistro() {
        return registro;
    }

    public void setRegistro(String registro) {
        this.registro = registro;
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

    public String getEstacion() {
        return estacion;
    }

    public void setEstacion(String estacion) {
        this.estacion = estacion;
    }

    public boolean isEn_transito() {
        return en_transito;
    }

    public void setEn_transito(boolean en_transito) {
        this.en_transito = en_transito;
    }

    public boolean isEstado_operativo() {
        return estado_operativo;
    }

    public void setEstado_operativo(boolean estado_operativo) {
        this.estado_operativo = estado_operativo;
    }
}
