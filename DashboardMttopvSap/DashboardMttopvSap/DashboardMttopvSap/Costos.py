import pandas as pd

class TablaCostos:
    
    @staticmethod
    def eliminar_columnas_innecesarias(df: pd.DataFrame) -> pd.DataFrame:
        """Elimina columnas innecesarias del DataFrame."""
        columnas_a_eliminar = [ 
            "Centro emplazamiento", "Área de empresa", "Centro planificación",
            "Ubicación técnica", "Equipo", "Conjunto", "SumCostPln.1",
            "SumCosReal.1", "CstSalInt.1", "CstSalExt.1",
            "CstMatProp.1", "CstMatExt.1", "Cst. serv..1",
            "Otros cst..1", "IngTotReal.1", "IngTotReal", "Otros cst.",
            "Parad.entr", "AvisRegist", "Núm.OrdMT", "CstSalExt"
        ]
        df = df.drop(columns=[col for col in columnas_a_eliminar if col in df.columns], errors='ignore')
        return df

    @staticmethod
    def eliminar_filas_todas_cero(df: pd.DataFrame) -> pd.DataFrame:
        """Elimina filas donde todas las columnas de costos son cero."""
        columnas_a_revisar = [
            'Costo Planificado', 'Costo Real', 'Costo Salario Interno',
            'Costo Material Propio', 'Costo Material Externo', 'Costo Servicio'
        ]
        for col in columnas_a_revisar:
            df[col] = df[col].str.replace('.', '', regex=False)
            df[col] = df[col].str.replace(',', '.', regex=False)
            df[col] = pd.to_numeric(df[col], errors='coerce')
        df = df[~(df[columnas_a_revisar] == 0).all(axis=1)]  # Elimina filas con ceros en todas las columnas de costos
        return df

    @staticmethod
    def Cambio_emplamazamiento(df: pd.DataFrame) -> pd.DataFrame:
        """Modifica los valores de la columna 'Emplazamiento'."""
        if "Emplazamiento" in df.columns:
            df["Emplazamiento"] = df["Emplazamiento"].replace({
                "PARQ": "A400",
                "PALMAS": "A400"
            })
        return df

    @staticmethod
    def convertir_mes_a_fecha(df: pd.DataFrame) -> pd.DataFrame:
        """Convierte el valor de la columna 'Mes' a formato de fecha."""
        df["Mes"] = "01." + df["Mes"].astype(str)
        df["Mes"] = pd.to_datetime(df["Mes"], format='%d.%m.%Y', errors='coerce')
        return df

    @staticmethod
    def renombra_columnas(df: pd.DataFrame) -> pd.DataFrame:
        """Renombra columnas según el diccionario especificado."""
        renombrar = {
            "SumCostPln": "Costo Planificado",
            "SumCosReal": "Costo Real",
            "CstSalInt": "Costo Salario Interno",
            "CstMatProp": "Costo Material Propio",
            "CstMatExt": "Costo Material Externo",
            "Cst. serv.": "Costo Servicio"
        }
        df.rename(columns=renombrar, inplace=True)
        return df