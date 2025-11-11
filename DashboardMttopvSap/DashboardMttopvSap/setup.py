from setuptools import setup, find_packages

setup(
    name="DashboardMttopvSap",   # nombre de tu paquete (como lo instalarás con pip)
    version="0.1.0",   # sube la versión según cambios (ej: 0.2.0 por mejoras)
    description="Paquete para limpieza y transformación de datos del Modulo PM de SAP",
    author="Carlos Zpa",
    author_email="calzapata18@Gmail.com",
    packages=find_packages(include=["DashboardMttopvSap", "DashboardMttopvSap.*"]),  # detecta módulos y submódulos
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.23.0"
    ],
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
