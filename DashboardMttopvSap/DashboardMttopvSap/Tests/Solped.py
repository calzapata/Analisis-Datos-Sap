import DashboardMttopvSap as tds

if __name__ == "__main__":
    df_Solped = tds.leerCsv(r"C:\Users\carlos.zapata\Documents\Archivos_Dash\Data\ME5A.csv", sep=',')

    df_Solped = tds.Solped.Eliminar_segun_pedido(df_Solped)
    df_Solped = tds.Solped.Limpiar_usuarios(df_Solped)
    df_Solped = tds.Solped.Convertir_Material(df_Solped)
    df_Solped = tds.Solped.Convertir_Indicador(df_Solped)
    set_data_solpe = tds.Solped.Convertir_Necesidad(df_Solped)

    print("=== Solped LIMPIAS ===")
    print(df_Solped.head(20))

    # 👉 Guardar resultados
    set_data_solpe.to_csv("Solped_limpia.csv", index=False, encoding="utf-8")
