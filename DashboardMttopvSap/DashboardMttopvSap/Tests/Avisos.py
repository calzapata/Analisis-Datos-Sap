import DashboardMttopvSap as tds

if __name__ == "__main__":

    df_Avisos = tds.leerCsv(r"C:\Users\carlos.zapata\Documents\Archivos_Dash\Data\IW28.csv", sep=',')

    df_Avisos = tds.Avisos.actualizar_status_aviso(df_Avisos)
    df_Avisos = tds.utils.columna_escenario(df_Avisos)
    df_Avisos = tds.utils.definir_region(df_Avisos)
    df_Avisos = tds.Avisos.Corregir_decimal(df_Avisos)
    df_Avisos = tds.Avisos.actualizar_class_aviso(df_Avisos)
    set_data_aviso = tds.utils.actualizar_grup_planif(df_Avisos)
    


    print("=== Avisos LIMPIAS ===")
    print(df_Avisos.head(20))

    # 👉 Guardar resultados
    df_Avisos.to_csv("Avisos_limpia.csv", index=False, encoding="utf-8")
