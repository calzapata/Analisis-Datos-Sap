import pandas as pd


class PuestosTrabajo:
    
    puestos_trabajo_mapping = {
        "M-PVAX01": "Jhonatan Valdez N°01",
        "M-PVFR01": "Wilson Restrepo N°01",
        "M-PVFR02": "Raul Moreno N°02",
        "M-PVFR03": "Gonzalo Gutierrez N°03",
        "M-PVFR04": "Giovanni Bolivar N°04",
        "M-PVFR05": "Sergio Cano N°05",
        "M-PVFR06": "Frigorista PV N°06",
        "M-PVFR07": "Frigorista PV N°07",
        "M-PVINFR": "Infraestructura PV",
        "M-PVM01": "Jader Tapias N°01",
        "M-PVM02": "Daniel Hincapie N°02",
        "M-PVM03": "Camilo Ramos N°03",
        "M-PVM04": "Josue Duarte N°04",
        "M-PVMETR": "Metrología PV",
        "M-PVML01": "Jhon Fredi Tuberquia N°01",
        "M-PVML02": "Carlos Bonilla N°02",
        "M-PVML03": "Ana Maria Gutierrez N°03",
        "M-PVML04": "Jorge Velez N°04",
        "M-PVOM01": "Darwin Jose Toscano N°01",
        "M-PVOM02": "Jaime Luis Lobo N°02",
        "M-PVOM03": "Oscar Arias N°03",
        "M-PVOM04": "Eglin Jose N°04",
        "M-PVOM05": "Nelson Dario Ochoa N°05",
        "M-PVOM06": "Jhon Edison N°06",
        "M-PVOM07": "Migel Arredondo N°07",
        "M-PVOM08": "Jhojan Cardona N°08",
        "M-PVOM09": "Wilmar Gonzales N°09",
        "M-PVOM10": "Wilmar Cardona N°10",
        "M-PVOM11": "Johan Vanegas N°11",
        "M-PVOM12": "Fabian Salcedo PV N°12",
        "M-PVQEM": "Equipos electromecánicos PV",
        "M-PVREFR": "Refrigeración y climatización PV",
        "M-PVSO01": "Josep Roa N°01",
        "M-PVSO02": "Carlos Pastrana N°02",
        "M-PVSV01": "Victor Cardona PV N°01",
        "M-PVSV02": "Supervisor PV N°02",
        "M-PVT01": "Rober Pinilla N°01",
        "M-PVT02": "Douglas Wladimi N°02",
        "M-PVT03": "Juan Barvaran N°03",
        "M-PVT04": "Dirley Arias N°04"
    }

    @staticmethod
    def Puestos_trabajo(df: pd.DataFrame) -> pd.DataFrame:
        if "Pto.tbjo.op." in df.columns:
            df["Pto.tbjo.op."] = df["Pto.tbjo.op."].replace(PuestosTrabajo.puestos_trabajo_mapping)
        return df

    @staticmethod
    def Costo_trabajo_real(df: pd.DataFrame) -> pd.DataFrame:
        if "Trabajo real" in df.columns:
            df["Trabajo real"] = pd.to_numeric(df["Trabajo real"], errors='coerce')
            df["Trabajo real"] = df["Trabajo real"] * 2
        return df
