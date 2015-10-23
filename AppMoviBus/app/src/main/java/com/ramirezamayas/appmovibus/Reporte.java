package com.ramirezamayas.appmovibus;

/**
 * Created by RamirezAmayaS on 10/23/15.
 */
public class Reporte {

    private String identificador;

    private String reserva;

    private String movibus;

    private String conductor;

    public Reporte(String identificador, String reserva, String movibus, String conductor) {
        this.identificador = identificador;
        this.reserva = reserva;
        this.movibus = movibus;
        this.conductor = conductor;
    }

    public String getIdentificador() {
        return identificador;
    }

    public void setIdentificador(String identificador) {
        this.identificador = identificador;
    }

    public String getReserva() {
        return reserva;
    }

    public void setReserva(String reserva) {
        this.reserva = reserva;
    }

    public String getMovibus() {
        return movibus;
    }

    public void setMovibus(String movibus) {
        this.movibus = movibus;
    }

    public String getConductor() {
        return conductor;
    }

    public void setConductor(String conductor) {
        this.conductor = conductor;
    }
}
