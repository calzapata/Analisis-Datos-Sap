
import DashboardMttopvSap as tds

if __name__ == "__main__":

    df_orden = tds.leerCsv(r"C:\Users\carlos.zapata\Documents\Archivos_Dash\Data\IW38.csv", sep=',')
    df_maestra_materiales = tds.leerCsv(r"C:\Users\carlos.zapata\Documents\Archivos_Dash\Data\Maestra_Materiales.csv", sep=',')
    df_material = tds.leerCsv(r"C:\Users\carlos.zapata\Documents\Archivos_Dash\Data\MB51.csv", sep=',')

    df_material = tds.Materiales.filtrar_filas_segun_orden(df_material, df_orden)
    df_material = tds.utils.actualizar_grup_planif(df_material)
    df_material = tds.utils.limpiar_columna_costos(df_material, "Impte.mon.local")
    df_material = tds.Materiales.ajustar_clase_movimiento(df_material)
    df_material = tds.Materiales.corregir_cantidades(df_material)
    df_material = tds.Materiales.clasificar_material(df_material)
    df_material = tds.Materiales.Limpiar_id_material(df_material)
    df_data_material = tds.Materiales.convertir_impte_mon_loc(df_material)
    df_maestra_materiales = tds.Materiales.Limpiar_id_material(df_maestra_materiales)

    print(df_material.head())
    df_data_material.to_csv("materiales_limpios.csv", index=False, encoding="utf-8-sig")