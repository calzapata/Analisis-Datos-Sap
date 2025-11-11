import pandas as pd

class utils:
    
    @staticmethod
    def actualizar_grup_planif(df: pd.DataFrame) -> pd.DataFrame:
        reemplazos = {
            "P41": "Electromecanico",
            "P42": "Frigoristas",
            "P43": "Infraestructura",
            "P44": "Metrologia",

            ######GRANJAS###########

            "P91": "Electromecanico",
            "P61": "Electromecanico",
            "P62": "Infraestructura",
            "P63": "Frigoristas",
            "P64": "Metrologia",
        }

        for col in ["Grupo planif.", "Grupo planificación"]:
            if col in df.columns:
                df[col] = df[col].replace(reemplazos)
        
        return df
    
    @staticmethod
    def limpiar_columna_costos(df: pd.DataFrame, columna: str) -> pd.DataFrame:
        if columna in df.columns:
            df[columna] = (
                df[columna]
                .astype(str)
                .str.replace('.', '', regex=False)
                .str.replace(',', '', regex=False)
            )
            df[columna] = pd.to_numeric(df[columna], errors='coerce')
        return df
    

    @staticmethod
    def definir_region(df: pd.DataFrame) -> pd.DataFrame:
        # Todas las zonas y regiones juntas, en orden de prioridad
        categorias = {
            "zona_fria": {"G100", "G250", "G300", "G550", "G570", "G580", "G600", "G650", "G700", "G750", "G850"},
            "zona_caliente": {"G880", "G870", "G590", "G500", "G450", "G400", "G350"},
            "zona_trampa": {"G150", "G200", "G560", "G800"},

            "Antioquia": {
                "C580", "C570", "C180", "C170", "C160", "C150", "C470", "C460", "C440", "C410", "C240", "C230",
                "C220", "C210", "C200", "C190", "C140", "C130", "C120", "C110", "C100", "A400", "A330", "A300",
                "A290", "A280", "A270", "A140", "A130", "A120", "A110"
            },

            "Zona Costera": {
                "C490", "C480", "C430", "C420", "C310", "C320", "C300", "C290", "C280", "C270", "C260",
                "A340", "A210", "A200", "A190", "A180", "A170", "A160", "C550", "C250"
            },

            "Valle": {"C400", "C390", "C380", "C370", "C360", "A260", "A250", "A240"},

            "Centro": {"C450", "C350", "C340", "C330", "A230", "A220"}
        }

        def get_region(code):
            for nombre, codigos in categorias.items():
                if code in codigos:
                    return nombre
            return "Sin región"

        col_codigo = next((col for col in ["Centro", "Ce.emplazam."] if col in df.columns), None)

        if col_codigo:
            df["region"] = df[col_codigo].apply(get_region)
        else:
            df["region"] = "Sin región"

        return df




    @staticmethod
    def columna_escenario(df: pd.DataFrame) -> pd.DataFrame:
        centros_puntos_venta = {
            "A110", "A120", "A130", "A140", "A150", "A160", "A170", "A180", "A190", "A200",
            "A210", "A220", "A230", "A240", "A250", "A260", "A270", "A280", "A290", "A300",
            "A330", "A340", "C100", "C110", "C120", "C130", "C140", "C150", "C160", "C170",
            "C180", "C190", "C200", "C210", "C220", "C230", "C240", "C250", "C260", "C270",
            "C280", "C290", "C300", "C310", "C320", "C330", "C340", "C350", "C360", "C370",
            "C380", "C390", "C400", "C410", "C420", "C430", "C440", "C460", "C470", "C570",
            "C580", "A400"
        }

        centros_granjas = {
            "G100", "G250", "G300", "G550", "G570", "G580", "G600", "G650", "G700", "G750",
            "G850", "G880", "G870", "G590", "G500", "G450", "G400", "G350", "G150", "G200",
            "G560", "G800"
        }

        def get_escenario(code):
            if code in centros_puntos_venta:
                return "Puntos de Venta"
            elif code in centros_granjas:
                return "Granjas"
            else:
                return "No definido"

        for col in ["Centro", "Ce.emplazam."]:
            if col in df.columns:
                df["escenario de negocios"] = df[col].apply(get_escenario)
                break
        return df

