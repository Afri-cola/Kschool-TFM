# Kschool-TFM
Final Project of the KSchool Master in Data Science (2020-2021)


Este estudio tiene por finalidad hacer un análisis de las variables macroeconómicas que mantienen una mayor correlación con la inversión española para que nos pueda ayudar en la toma de decisiones a la hora de buscar diferentes targets. En concreto nos centraremos en el país de México.

Las variables macroeconómicas que se utilizadas en el estudio son:
- PIB
- IPC
- Balanza de pagos
- Tasa de desempleo
- Exportaciones
- Importaciones
- Inversión Extranjera Directa (IED)
- IPC
- PIB
- Deuda pública
- Reservas
- Tasa de interés

Se han seleccionado estas variables porque son las que Bank of America (BoA) utiliza para medir el riesgo del negocio basado en razones económicas y financieras.

El estudio está dividido en diferentes fases:
1. Extracción del dato
2. Lectura y análisis de las variables
3. Estudio del conjunto de variables
4. Modelo de regresión
5. Análisis de la inversión española en México y de la inversión extranjera directa (IED) de México.


Tras aplicar los diferentes métodos para solucionar la multicolinealidad, nos quedamos con el modelo que nos da el VIF ya que tiene un error menor (0.44) que el de PCA y PCR (0.76).

El modelo de regresión lineal múltiple es:

Inversion ES = -0.0463 -0.4225IPC + 0.0625Desempleo - 0.3171IED + 0.9429Deuda Externa -0.0135Saldo Balanza Pagos

Es capaz de explicar el 83.1% de la varianza observada en la inversión española . El test F es (p-value = 0.00000268), por lo que se puede aceptar que  la relación observada no se debe al azar (p-value ≈ 0).
