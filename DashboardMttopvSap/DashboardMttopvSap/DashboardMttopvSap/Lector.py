import pandas as pd

def leerCsv(path: str, sep: str = ";", encoding: str = "utf-8", on_bad_lines: str = "skip") -> pd.DataFrame:
    return pd.read_csv(path, sep=sep, encoding=encoding, on_bad_lines=on_bad_lines)

def leerExcel(path: str, sheet_name: str = None) -> pd.DataFrame:
    return pd.read_excel(path, sheet_name=sheet_name)
