import statistics as st
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Os dados a seguir foram coletados para determinar a relação entre duas variáveis de 
# processamento e a dureza de certo tipo de aço 
# dureza 


xT = np.array([[0.02, 1000], [0.02, 1200], [0.10, 1000], [0.10, 1200], [0.18, 1000], [0.18, 1200]])
yT = np.array([78.9, 55.2, 80.9, 57.4, 85.3, 60.7])


print("Ex1 - Ajuste uma equação da reta para os dados fornecidos")

x_const = sm.add_constant(xT)
modelo = sm.OLS(yT, x_const) 
resultado = modelo.fit()
print(resultado.summary())


print("""Ex2 - Utilize essa equação para estimar a dureza do aço quando o conteúdo de cobre é 
de 0,14% e a temperatura de têmpera for de 1100 F° """)

valor = sm.add_constant([[0.14, 1100]])
durezaEstimado = resultado.predict(valor)
print(round(durezaEstimado[0], 2))
