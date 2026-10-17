# %% Importacion de librerias

#Manejar rutas relativas
from pathlib import Path #manejar rutas relativas 

#
import pandas as pd #manejo de bases de datos
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import jarque_bera, probplot # type: ignore

#
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.stats.diagnostic import acorr_ljungbox, het_arch, acorr_breusch_godfrey

# %% Base de datos

#Obtener ruta de directorio
Base_Dir = Path(__file__).resolve().parents[0]     #__file__ hace referencia al archivo actual de pyhton

# Obtener ruta del directorio de la base de datos
Directorio = Base_Dir / "Base de datos"

#Rutas de la base de datos
Ruta = Directorio / "Base de datos - Poster.xlsx"
# %% Data frame

df = pd.read_excel(Ruta, sheet_name="Datos", skiprows=[1])

# %%
