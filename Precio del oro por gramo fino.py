# $$$$$$$\                                $$\                 
# $$  __$$\                               \__|                
# $$ |  $$ | $$$$$$\   $$$$$$\   $$$$$$$\ $$\  $$$$$$\        
# $$$$$$$  |$$  __$$\ $$  __$$\ $$  _____|$$ |$$  __$$\       
# $$  ____/ $$ |  \__|$$$$$$$$ |$$ /      $$ |$$ /  $$ |      
# $$ |      $$ |      $$   ____|$$ |      $$ |$$ |  $$ |      
# $$ |      $$ |      \$$$$$$$\ \$$$$$$$\ $$ |\$$$$$$  |      
# \__|      \__|       \_______| \_______|\__| \______/                                                                 
#       $$\           $$\                                     
#       $$ |          $$ |                                    
#  $$$$$$$ | $$$$$$\  $$ |       $$$$$$\   $$$$$$\   $$$$$$\  
# $$  __$$ |$$  __$$\ $$ |      $$  __$$\ $$  __$$\ $$  __$$\ 
# $$ /  $$ |$$$$$$$$ |$$ |      $$ /  $$ |$$ |  \__|$$ /  $$ |
# $$ |  $$ |$$   ____|$$ |      $$ |  $$ |$$ |      $$ |  $$ |
# \$$$$$$$ |\$$$$$$$\ $$ |      \$$$$$$  |$$ |      \$$$$$$  |
#  \_______| \_______|\__|       \______/ \__|       \______/ 



#  Importando bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import warnings
warnings.filterwarnings('ignore')

