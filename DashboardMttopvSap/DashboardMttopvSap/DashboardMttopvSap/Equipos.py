import pandas as pd
import unicodedata

class Equipos:
    @staticmethod
    def eliminar_filas_con_dato_equipo_superior(df: pd.DataFrame) -> pd.DataFrame:
        if "Equipo superior" in df.columns:
            df = df[df["Equipo superior"].isnull()]  # Filtra las filas donde 'Equipo superior' es nulo
        return df

    @staticmethod
    def eliminar_columna(df: pd.DataFrame) -> pd.DataFrame:
        if "Equipo superior" in df.columns:
            df = df.drop(columns=["Equipo superior"])  # Elimina la columna 'Equipo superior'
        return df

    @staticmethod
    def Modificar_calumna_Status(df: pd.DataFrame) -> pd.DataFrame:
        if "Status usuario" in df.columns:
            df.loc[df["Status usuario"].str.startswith("FUNC", na=False), "Status usuario"] = "Operativo"
            df.loc[df["Status usuario"].str.startswith("BAJA", na=False), "Status usuario"] = "Fuera de Servicio"
            df.loc[df["Status usuario"].str.startswith("ENRE", na=False), "Status usuario"] = "En Reparacion"
        return df

    @staticmethod
    def Asignacion_equipos(df: pd.DataFrame) -> pd.DataFrame:
        palabras_grupo = {
            "vitrina cong": "Vitrina congelacion",
            "vitrina refri": "Vitrinas refrigeracion",
            "condensadora linea": "Vitrinas refrigeracion",
            "rack de refri": "Vitrinas refrigeracion",
            "controlador vitrina": "Vitrinas refrigeracion",
            "controlador line": "Vitrinas refrigeracion",
            "unidad congela": "Cava de congelacion",
            "condensador cava congel": "Cava de congelacion",
            "evaporador cava conge": "Cava de congelacion",
            "controlador cava conge": "Cava de congelacion",
            "unidad refrig": "Cava de refrigeracion",
            "evaporador cava refrig": "Cava de refrigeracion",
            "controlador cava refrig": "Cava de refrigeracion",
            "condensador cava refrig": "Cava de refrigeracion",
            "aire": "Aires Acondicionados",
            "nevera horizo": "Nevera horizontal",
            "controlador nevera horizon": "Nevera horizontal",
            "nevera domest": "Nevera domestica",
            "indicador tempe nevera domest": "Nevera domestica",
            "indicador tempe nevera verti": "Nevera domestica",
            "controlador nevera conge": "Nevera vertical congelacion",
            "controlador nevera vert conge": "Nevera vertical congelacion",
            "nevera vertical congel": "Nevera vertical congelacion",
            "nevera vertical refrige": "Nevera vertical refrigeracion",
            "controlador nevera refrige": "Nevera vertical refrigeracion",
            "nevera refrigeracion vert": "Nevera vertical refrigeracion",
            "nevera vertical mixta": "Nevera mixta",
            "controlador modulo conge": "Nevera mixta",
            "controlador modulo refrig": "Nevera mixta",
            "balanza etiqueta": "Balanzas etiqueta",
            "bascula plataforma": "Balanza plataforma",
            "balanza repes": "Balanza repeso",
            "balanza colgan": "Balanza colgante",
            "termometro punc": "Termometro de punzon",
            "sierra": "Sierras sin fin",
            "sistema bombe": "Bomba",
            "bomba": "Bomba",
            "molin": "Molino",
            "freidora electr": "Freidora electrica",
            "freidora a gas": "Freidora a gas",
            "extracto": "Extractor",
            "plancha": "Plancha",
            "parrilla": "Equipos de cocción",
            "fogon": "Fogon a gas",
            "malacate": "Malacate",
            "planta elect": "Planta electrica",
            "tajadora": "Tajadora",
        }
        
        def quitar_tildes(texto: str) -> str:
            # Normaliza el texto eliminando las tildes
            nfkd = unicodedata.normalize('NFKD', texto)
            return ''.join([c for c in nfkd if not unicodedata.combining(c)])

        if "Descripción" in df.columns:
            # Convertir a minúsculas, eliminar tildes y asignar el texto normalizado
            df["Descripción"] = df["Descripción"].fillna("").astype(str).apply(lambda x: quitar_tildes(x).lower())
            df["asignacion_equipos"] = None

            def asignar_equipo(descripcion: str) -> str:
                for palabra, grupo in palabras_grupo.items():
                    # Realizamos la búsqueda en la versión normalizada de la descripción
                    if palabra in descripcion:
                        return grupo
                return "Equipo no clasificado"

            # Aplicar la función de asignación a la columna normalizada
            df["asignacion_equipos"] = df["Descripción"].apply(asignar_equipo)
        
        return df
