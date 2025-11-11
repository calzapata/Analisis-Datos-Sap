import DashboardMttopvSap as tds

if __name__ == "__main__":
    df_Equipos = tds.leerCsv(r"C:\Users\carlos.zapata\Documents\Archivos_Dash\Data\IE05.csv", sep=',')

    df_Equipos = tds.Equipos.eliminar_filas_con_dato_equipo_superior(df_Equipos)
    df_Equipos = tds.Equipos.eliminar_columna(df_Equipos)
    df_Equipos = tds.Equipos.Modificar_calumna_Status(df_Equipos)
    set_data_equipo = tds.Equipos.Asignacion_equipos(df_Equipos)

    print("=== Equipos LIMPIAS ===")
    print(df_Equipos.head(20))

    # 👉 Guardar resultados
    df_Equipos.to_csv("Equipos_limpia.csv", index=False, encoding="utf-8")
