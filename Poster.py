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
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.stats.diagnostic import acorr_ljungbox, het_arch, acorr_breusch_godfrey

# %% Base de datos

#Obtener ruta de directorio
Base_Dir = Path(__file__).resolve().parent    #__file__ hace referencia al archivo actual de pyhton

#Rutas de la base de datos
Ruta_Precio_Oro = Base_Dir / "Base de datos - Poster.xlsx"
# %% Data frame
precio_oro_df = pd.read_excel(Ruta_Precio_Oro, sheet_name="Datos", skiprows=[1])
print(type(precio_oro_df))

print(precio_oro_df.head())
print(precio_oro_df.info())

precio_oro_df.index = pd.to_datetime(precio_oro_df["Fecha"])

# %%Creacion Series de tiempo

#La serie de tiempo se va a llamar precio_oro_serie y se va a crear a partir de la columna "Precio" del DataFrame precio_oro_df.
precio_serie = precio_oro_df["Precio"].copy()
precio_serie = pd.to_numeric(precio_serie, errors="coerce")
precio_serie = precio_serie.dropna()

print(precio_serie.head())
print(precio_serie.info())

print(type(precio_serie))
print(precio_serie.describe())
# %% =========================
#   PASO 1: Idetificacion
#=============================

#Grafico de la serie de tiempo
plt.figure(figsize=(12, 6))
plt.plot(precio_serie, color="blue", label="Precio del oro")
plt.xlabel("Fecha")
plt.ylabel("Precio")
plt.title("Serie de tiempo: Precio del oro")
plt.legend()
plt.show()
# %%FAC Y FACP

fig,axes = plt.subplots(1,2,figsize=(14,6))

plot_acf(
    precio_serie,
    lags=24,
    alpha=0.05,
    bartlett_confint=False,
    ax=axes[0]
)
axes[0].set_title("FAC")

plot_pacf(
    precio_serie,
    lags=24,
    alpha=0.05,
    ax=axes[1]
)
axes[1].set_title("FACP")
# %%Test de Raiz Unitaria

adf_result = adfuller(precio_serie)

print(".\n----Test de Raiz Unitaria ADF----")
print("Estadistico ADF:", adf_result[0])
print("Valor-p:", adf_result[1])
print("Rezagos usados:", adf_result[2])
print("Observaciones usadas:", adf_result[3])
print("Valores criticos:")
for nivel, valor in adf_result[4].items():
    print(f"  {nivel}: {valor}")

if adf_result[1] < 0.05:
    print("ADF: Rechazamos H0. La serie es estacionaria según el test ADF.")
else:
    print("ADF: No rechazamos H0. La serie no es estacionaria según el test ADF.")

# %% Diferenciar la serie de tiempo

precio_serie_diff = precio_serie.diff().dropna()

plt.figure(figsize=(12, 6))
plt.plot(precio_serie_diff, color="blue", label="Precio del oro (diferenciado)")
plt.xlabel("Fecha")     
plt.ylabel("Precio Diferenciado")
plt.title("Serie de tiempo: Precio del oro (diferenciado)")
plt.grid(True)
plt.show()

# %%Diferencia del logaritmo de la serie de tiempo

precio_serie_logdiff = np.log(precio_serie).diff().dropna()

plt.figure(figsize=(12, 6))
plt.plot(precio_serie_logdiff, color="blue", label="Precio del oro (log-diferenciado)")
plt.xlabel("Fecha")
plt.ylabel("Log(Precio) Diferenciado")
plt.title("Serie de tiempo: Precio del oro (logaritmo diferenciado)")
plt.grid(True)
plt.show()
# %% FAC y FACP de la serie log-diferenciada    

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

plot_acf(
    precio_serie_logdiff,
    lags=24,
    alpha=0.05,
    bartlett_confint=False,
    ax=axes[0]
)
axes[0].set_title("FAC")

plot_pacf(
    precio_serie_logdiff,
    lags=24,
    alpha=0.05,
    ax=axes[1]
)
axes[1].set_title("FACP")
# %%adf a la serie log-diferenciada

adf_result_logdiff = adfuller(precio_serie_logdiff)

print("\n----Test de Raiz Unitaria ADF (Log-Diferenciado)----")
print("Estadistico ADF:", adf_result_logdiff[0])
print("Valor-p:", adf_result_logdiff[1])
print("Rezagos usados:", adf_result_logdiff[2]) 
print("Observaciones usadas:", adf_result_logdiff[3])
print("Valores criticos:")
for nivel, valor in adf_result_logdiff[4].items():
    print(f"  {nivel}: {valor}")

if adf_result_logdiff[1] < 0.05:
    print("ADF: Rechazamos H0. La serie log-diferenciada es estacionaria según el test ADF.")
else:
    print("ADF: No rechazamos H0. La serie log-diferenciada no es estacionaria según el test ADF.")


# %%
