import pandas as pd


class Avisos:
    
    clase_aviso_mapping = {
        "MC": "Correctivo",
        "MF": "Fabricacion",
        "MZ": "Correctivo",
        "MT": "Instalacion"
    }

    @staticmethod
    def actualizar_status_aviso(df: pd.DataFrame) -> pd.DataFrame:
        
        df.loc[df["Status sistema"].str.startswith(("MECE","ENER","AUOK"), na=False), "Status sistema"] = "Cerrado"
        df.loc[df["Status sistema"].str.startswith(("METR","MDIF","AUTO"), na=False), "Status sistema"] = "Tratamiento"
        df.loc[df["Status sistema"].str.startswith("MEAB", na=False), "Status sistema"] = "Abierto"
        return df

    @staticmethod
    def Corregir_decimal(df: pd.DataFrame) -> pd.DataFrame:
        if "Duración parada" in df.columns:
            df["Duración parada"] = df["Duración parada"].astype(str)
            df["Duración parada"] = df["Duración parada"].str.split(',', n=1).str[0]
            df["Duración parada"] = pd.to_numeric(df["Duración parada"], errors='coerce')
        return df

    @staticmethod
    def actualizar_class_aviso(df: pd.DataFrame) -> pd.DataFrame:
        if "Clase de aviso" in df.columns:
            df["Clase de aviso"] = df["Clase de aviso"].replace(Avisos.clase_aviso_mapping)
        return df
    
    ###NO SE ESTA USANDO #########
    @staticmethod
    def eliminar_avisos_sin_orden(df: pd.DataFrame) -> pd.DataFrame:
        if "Orden" in df.columns:
            df = df[df["Orden"].notna() & (df["Orden"] != "")]
        return df
