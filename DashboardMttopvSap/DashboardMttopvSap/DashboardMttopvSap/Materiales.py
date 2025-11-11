import pandas as pd
import numpy as np


class Materiales:

    @staticmethod
    def clasificar_material(df: pd.DataFrame) -> pd.DataFrame:
        if "Material" in df.columns:
            materiales = df["Material"].fillna("").astype(str)
            df["Clase de pedido"] = materiales.apply(
                lambda x: "Servicio" if x.strip() == "" else "Material"
            )
        return df

    @staticmethod
    def ajustar_clase_movimiento(df: pd.DataFrame) -> pd.DataFrame:
        if "Clase de movimiento" not in df.columns:
            return df

        clase_norm = df["Clase de movimiento"].astype(str)

        if "Material" in df.columns:
            material_vacio = df["Material"].fillna("").astype(str).str.strip() == ""
            material_no_vacio = ~material_vacio

            condiciones = [
                (clase_norm == "101") & material_no_vacio,
                (clase_norm == "101") & material_vacio,
                (clase_norm == "102") & material_no_vacio,
                (clase_norm == "102") & material_vacio,
                (clase_norm == "122") & material_no_vacio,
                (clase_norm == "261") & material_no_vacio,
                (clase_norm == "262") & material_no_vacio
            ]

            resultados = [
                "Compra de material",
                "Servicio Externo",
                "Compra Anulado",
                "Servicio Cancelado",
                "Compra Anulado",
                "Salida Material orden",
                "Devolucion Material orden"
            ]

            df["Clase de movimiento"] = np.select(condiciones, resultados, default=df["Clase de movimiento"])

        return df

    @staticmethod
    def Limpiar_id_material(df: pd.DataFrame) -> pd.DataFrame:
        if "Material" in df.columns:
            # Convertir a string, eliminar nulos, espacios y '.0' del final
            s = df["Material"].astype(str).str.strip().replace('nan', '')
            s = s.str.replace(r'\.0$', '', regex=True)
            s = s.mask(s == '', '99999999')

            df["Material"] = s

        return df

    @staticmethod
    def corregir_cantidades(df: pd.DataFrame) -> pd.DataFrame:
        if "Cantidad" not in df.columns:
            return df

        df["Cantidad"] = pd.to_numeric(df["Cantidad"], errors='coerce').fillna(0)

        if "Clase de movimiento" not in df.columns:
            return df

        mask_salida = df["Clase de movimiento"].eq("Salida Material orden")
        df.loc[mask_salida, "Cantidad"] = df.loc[mask_salida, "Cantidad"].abs()

        mask_devolucion = df["Clase de movimiento"].eq("Devolucion Material orden")
        df.loc[mask_devolucion, "Cantidad"] = -df.loc[mask_devolucion, "Cantidad"].abs()

        return df

    @staticmethod
    def filtrar_filas_segun_orden(df_material: pd.DataFrame, df_orden: pd.DataFrame) -> pd.DataFrame:
        if "Orden" not in df_material.columns or "Orden" not in df_orden.columns:
            return df_material

        df_material['Orden'] = df_material['Orden'].astype(str)
        df_orden['Orden'] = df_orden['Orden'].astype(str)
        df_filtrado = df_material[df_material['Orden'].isin(df_orden['Orden'])].copy()

        df_orden_reducido = df_orden[['Orden', 'Grupo planif.']].drop_duplicates()
        df_resultado = df_filtrado.merge(df_orden_reducido, on='Orden', how='left')

        return df_resultado

    @staticmethod
    def convertir_impte_mon_loc(df: pd.DataFrame) -> pd.DataFrame:
        if "Impte.mon.local" in df.columns:
            s = pd.to_numeric(df["Impte.mon.local"], errors='coerce').fillna(0.0)
            if "Clase de movimiento" in df.columns:
                cm = df["Clase de movimiento"].astype(str)
                mask_dev = cm == "Devolucion Material orden"
                mask_sal = cm == "Salida Material orden"

                s.loc[mask_dev] = -s.loc[mask_dev].abs()
                s.loc[mask_sal] = s.loc[mask_sal].abs()

            df["Impte.mon.local"] = s
        return df
