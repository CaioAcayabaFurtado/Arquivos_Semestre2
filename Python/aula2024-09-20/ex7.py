import statistics as st
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Os dados a seguir representam as eficácias percentuais de um analgésico e a quantidade 
# em miligramas de três medicamentos presentes em cada cápsula 

xT = np.array([[15, 20, 10], [15, 20, 10], [15, 20, 10], [15, 20, 10], [30, 20, 20], [30, 20, 20], [30, 30, 20], [30, 30, 20], [45, 30, 20], [45, 30, 20]])
yT = np.array([47, 54, 58, 66, 59, 67, 71, 83, 85, 94])

print("""Ex1 - Calcule a equação de regressão, comentando sobre a qualidade da reta 
encontrada. """)

x_const = sm.add_constant(xT)
modelo = sm.OLS(yT, x_const) 
resultado = modelo.fit()
print(resultado.summary())

print("Considerando o PValue, o valor dele está muito alto, indicando que a qualidade da correlaçao é ruim")

print("""Ex2 - Utilize essa equação para estimar a eficácia percentual média de cápsulas 
contendo 12,5 mg do medicamento A, 25 mg do medicamento B e 15 mg do 
medicamento C """)

valor = sm.add_constant([[12.5, 25, 15]])
eficaciaEstimada = resultado.predict(valor)
print(round(eficaciaEstimada[0], 2))