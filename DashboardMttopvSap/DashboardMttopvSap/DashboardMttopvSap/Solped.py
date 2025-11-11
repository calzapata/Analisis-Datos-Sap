import pandas as pd
import re

class Solped:
    
    @staticmethod
    def Limpiar_usuarios(df: pd.DataFrame) -> pd.DataFrame:
        """ Filtra los datos manteniendo solo ciertos usuarios """
        Usuarios_mantener = ["JPESCOBAR", "CZAPATA", "VHCARDONA", "JDUARTE","AGUTIERREZ", "JTUBERQUIA", "MCCANO", "NVELEZ", "SCANO"]
        
        df.columns = df.columns.str.strip().str.lower()
        if "creado por" in df.columns:
            df = df[df["creado por"].isin(Usuarios_mantener)]
        return df

    @staticmethod
    def Convertir_Material(df: pd.DataFrame) -> pd.DataFrame:
        if "material" in df.columns:
            df["material"] = df["material"].apply(lambda x: "Material externo" if pd.notnull(x) and x != "" else "Servicio externo")
        return df

    @staticmethod
    def Convertir_Indicador(df: pd.DataFrame) -> pd.DataFrame:
        """ Convierte los indicadores de liberación a etiquetas legibles """
        if "indicador liberación" in df.columns:
            df["indicador liberación"] = df["indicador liberación"].replace({"4": "Liberado", "X": "No liberado"})
        return df
    
    @staticmethod
    def Eliminar_segun_pedido(df: pd.DataFrame) -> pd.DataFrame:
        if "Cantidad pedida" in df.columns:
            df = df[df["Cantidad pedida"].astype(float) != 0]
        return df

    @staticmethod
    def Convertir_Necesidad(df: pd.DataFrame) -> pd.DataFrame:
        if "número de necesidad" in df.columns:
            df["número de necesidad"] = df["número de necesidad"].fillna("").astype(str).str.upper()
            df["número de necesidad"] = df["número de necesidad"].replace({
                "COMPRA PV": "Compras Punto de venta",
                "BORRADO": "Compras Punto de venta",
                "URGENTE": "Compras Urgentes",
                "": "Compras Planificadas",
            })
            
            # Validación para fechas en formato dd.mm.yyyy
            fecha_pattern = r'^\d{1,2}\.\d{1,2}\.\d{2,4}$'
            df["número de necesidad"] = df["número de necesidad"].apply(
                lambda x: "Compras Planificadas" if re.match(fecha_pattern, x) else x
            )
        return df

