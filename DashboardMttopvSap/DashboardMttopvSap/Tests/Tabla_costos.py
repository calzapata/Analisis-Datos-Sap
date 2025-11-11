import DashboardMttopvSap as tds

if __name__ == "__main__":

    df_TablaCostos = tds.leerCsv(r"C:\Users\carlos.zapata\Documents\Archivos_Dash\Data\Analisis_Grup.csv", encoding='ISO-8859-1')

    df_TablaCostos = tds.utils.actualizar_grup_planif(df_TablaCostos)   
    df_TablaCostos = tds.TablaCostos.renombra_columnas(df_TablaCostos)
    df_TablaCostos = tds.TablaCostos.eliminar_filas_todas_cero(df_TablaCostos) #
    df_TablaCostos = tds.TablaCostos.Cambio_emplamazamiento(df_TablaCostos)
    df_TablaCostos = tds.TablaCostos.convertir_mes_a_fecha(df_TablaCostos)
    set_data_Analisis_grup = tds.TablaCostos.eliminar_columnas_innecesarias(df_TablaCostos) #
     

    print("=== TablaCostos LIMPIAS ===")
    print(df_TablaCostos.head(20))

    # 👉 Guardar resultados
    df_TablaCostos.to_csv("TablaCostos_limpia.csv", index=False, encoding="utf-8")
