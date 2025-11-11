import pandas as pd


class Orden:
    
    @staticmethod
    def actualizar_status_Orden(df: pd.DataFrame) -> pd.DataFrame:
        df.loc[df["Status sistema"].str.startswith("CTEC", na=False), "Status sistema"] = "Cerrado"
        df.loc[df["Status sistema"].str.startswith("LIB.", na=False), "Status sistema"] = "Liberado"
        df.loc[df["Status sistema"].str.startswith("ABIE", na=False), "Status sistema"] = "Abierto"
        return df


    @staticmethod
    def actualizar_clase_orden(df: pd.DataFrame) -> pd.DataFrame:
        if "Clase de orden" in df.columns:
            df["Clase de orden"] = df["Clase de orden"].replace({
                "MP01": "Correctivo",
                "PM01": "Correctivo",
                "MP02": "Preventivo",
                "MQ05": "Preventivo"
            })
        return df

    @staticmethod
    def atecion_oportuna(df: pd.DataFrame) -> pd.DataFrame:
        df["Fecha creación"] = pd.to_datetime(df["Fecha creación"], errors="coerce", dayfirst=True)
        df["Fecha fin real"] = pd.to_datetime(df["Fecha fin real"], errors="coerce", dayfirst=True)
        df["Dia_promedio"] = (df["Fecha fin real"] - df["Fecha creación"]).dt.days
        df["Dia_promedio"] = df["Dia_promedio"].fillna(0).astype(int)
        return df

    @staticmethod
    def grup_equip(df: pd.DataFrame) -> pd.DataFrame:
        palabras_grupo = {
            # Refrigeración
            "vitrina cong": "Vitrinas",
            "vitrina refri": "Vitrinas",
            "condensadora linea": "Vitrinas",
            "rack de refri": "Vitrinas",
            "controlador vitrina": "Vitrinas",
            "controlador line": "Vitrinas",
            "controlador sal": "Cavas",
            "cava": "Cavas",
            "unidad": "Cavas",
            "condensador cava": "Cavas",
            "evaporador": "Cavas",

            "aire": "Aires Acondicionados",
            "nevera horizo": "Neveras",
            "controlador nevera horizon": "Neveras",
            "base ch": "Neveras",
            "nevera vertical mixta": "Neveras",
            "controlador modulo conge": "Neveras",
            "controlador modulo refrig": "Neveras",
            "nevera": "Neveras",
            "dispensador de ag": "Neveras",
            "indicador tempe nevera do": "Neveras",

            # Metrología
            "balanza etiqueta": "Otras Balanzas",
            "bascula plataforma": "Otras Balanzas",
            "balanza repes": "Otras Balanzas",
            "balanza colgan": "Balanza colgante",
            "termometro": "equipos de medicion",
            "alcoholimetro": "equipos de medicion",

            # Electromecánico
            "sierra": "Equipos de corte",
            "tajadora": "Equipos de corte",

            "sistema bombe": "Bomba",
            "bomba": "Bomba",
            "dispensador lubricante": "dispensador lubricante",
            "electrodomesticos men": "Electrodomesticos",
            "peveceador": "Electrodomesticos",
            "procesador de ve": "Electrodomesticos",
            "puerta autom": "puertas automáticas",

            "molin": "Molino",
            "freidora intelig": "equipos de coccion",
            "freidora electr": "equipos de coccion",
            "freidora a gas": "equipos de coccion",
            "extracto": "equipos de coccion",
            "plancha": "equipos de coccion",
            "parrilla": "equipos de coccion",
            "fogon": "equipos de coccion",

            "malacate": "Malacate",
            "planta elect": "Respaldo electrico",
            "ups": "Respaldo electrico",
            "cam pv": "Red Datos",
        }

        if "Descripción" in df.columns:
            df["Descripción"] = df["Descripción"].fillna("").astype(str).str.lower()

        if "Grupo planif." in df.columns:
            df["Grupo planif."] = df["Grupo planif."].fillna("").astype(str).str.lower()

        if "Ubicac.técnica" in df.columns:
            df["Ubicac.técnica"] = df["Ubicac.técnica"].fillna("").astype(str)

        if "Grupo" not in df.columns:
            df["Grupo"] = None

        def asignar_grupo(row):
            if pd.notna(row["Grupo"]) and row["Grupo"].strip() != "":
                return row["Grupo"]

            descripcion = row.get("Descripción", "")
            planif = row.get("Grupo planif.", "")
            ubicacion = row.get("Ubicac.técnica", "")

            for palabra, grupo in palabras_grupo.items():
                if palabra in descripcion:
                    return grupo

            if "infraestructura" in planif:
                return "Grupo Infraestructura"

            if ubicacion.endswith("810"):
                return "Red Agua"
            elif ubicacion.endswith("820"):
                return "Red Electrica"
            elif ubicacion.endswith("880"):
                return "Red Sanitaria"
            elif ubicacion.endswith("830"):
                return "Red Datos"
            elif ubicacion.endswith("860"):
                return "Red de Gas"
            elif ubicacion.endswith("CAVREF"):
                return "Cavas"
            elif ubicacion.endswith("CAVCON"):
                return "Cavas"

            return "Grupo Infraestructura"

        df["Grupo"] = df.apply(asignar_grupo, axis=1)
        return df

    @staticmethod
    def Asignacion_equipos(df: pd.DataFrame) -> pd.DataFrame:
        palabras_grupo = {
            # Refrigeración
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

            # Metrología
            "balanza etiqueta": "Balanzas etiqueta",
            "bascula plataforma": "Balanza plataforma",
            "balanza repes": "Balanza repeso",
            "balanza colgan": "Balanza colgante",
            "termometro punc": "Termometro de punzon",

            # Electromecánico
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

        if "Descripción" in df.columns:
            df["Descripción"] = df["Descripción"].fillna("").astype(str).str.lower()

        df["asignacion_equipos"] = None

        def asignar_equipo(descripcion):
            for palabra, grupo in palabras_grupo.items():
                if palabra.lower() in descripcion:
                    return grupo
            return None

        df["asignacion_equipos"] = df["Descripción"].apply(asignar_equipo)

        return df

