import DashboardMttopvSap as tds

if __name__ == "__main__":

    df_orden = tds.leerCsv(r"C:\Users\carlos.zapata\Documents\Archivos_Dash\Data\IW38.csv", sep=',')

    df_orden = tds.utils.actualizar_grup_planif(df_orden)
    df_orden = tds.utils.limpiar_columna_costos(df_orden, "Cst.tot.reales")
    df_orden = tds.utils.definir_region(df_orden)
    df_orden = tds.Orden.actualizar_status_Orden(df_orden)
    df_orden = tds.Orden.atecion_oportuna(df_orden)
    df_orden = tds.Orden.actualizar_clase_orden(df_orden)
    df_orden = tds.Orden.grup_equip(df_orden)
    set_data_orden = tds.Orden.Asignacion_equipos(df_orden)



    # 👉 Verificación por consola
    print("=== ORDENES LIMPIAS ===")
    print(df_orden.head(20))
    print("\n=== MATERIALES LIMPIOS ===")
    #print(df_material.head())

    # 👉 Guardar resultados
    df_orden.to_csv("orden_limpia.csv", index=False, encoding="utf-8")
