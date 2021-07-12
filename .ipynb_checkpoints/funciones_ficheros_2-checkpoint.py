{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def tipo_cambio(root):\n",
    "    \n",
    "    \"\"\"Esta función lee el fichero con la variable. \n",
    "    Se transforma la variable de dolares a euros aplicando el tipo de cambio anual.\n",
    "    La variable se mide en millones de € y se redondea en dos decimales.\n",
    "    \n",
    "    \"\"\"\n",
    "    \n",
    "    df_export = pd.read_csv(root, header=0)\n",
    "    df_export.rename(columns={'Country Name':'country', 'Indicator Name':'variables' }, inplace=True)\n",
    "    df_export = df_export[df_export.country == 'México']\n",
    "    df_export['country'] = df_export['country'].replace('México', 'MEXICO')\n",
    "    df_export = df_export.drop(['Indicator Code', 'Country Code', 'country'], axis=1)\n",
    "    \n",
    "    root = 'Tipo de cambio- Dolar a Euro.csv'\n",
    "\n",
    "    df = pd.read_csv(root)\n",
    "    df.rename(columns={'Unnamed: 0' : 'variables'}, inplace=True)\n",
    "    var_name = df_export.loc[152].iloc[0]\n",
    "    df= df.replace({'Tipo de cambio': var_name})\n",
    "    df.set_index('variables', inplace=True)\n",
    "    \n",
    "    \n",
    "    df_export.set_index('variables', inplace=True)\n",
    "    df_export = df_export.div(1000000)\n",
    "    df_export = df_export.mul(df, axis=0)\n",
    "    \n",
    "    df_export = df_export.round(2)\n",
    "    df_export = df_export.transpose()\n",
    "    \n",
    "    return df_export.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "root = 'Variables_economicas/balanza de pagos.csv'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>variables</th>\n",
       "      <th>Saldo en cuenta corriente (balanza de pagos, US$ a precios actuales)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1993</th>\n",
       "      <td>-20811.96</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1994</th>\n",
       "      <td>-23809.78</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1995</th>\n",
       "      <td>-1177.13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1996</th>\n",
       "      <td>-1986.39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1997</th>\n",
       "      <td>-7001.92</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "variables  Saldo en cuenta corriente (balanza de pagos, US$ a precios actuales)\n",
       "1993                                               -20811.96                   \n",
       "1994                                               -23809.78                   \n",
       "1995                                                -1177.13                   \n",
       "1996                                                -1986.39                   \n",
       "1997                                                -7001.92                   "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tipo_cambio_2(root)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>variables</th>\n",
       "      <th>Deuda externa acumulada, total (DOD, US$ a precios actuales)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1993</th>\n",
       "      <td>117269.60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1994</th>\n",
       "      <td>112309.71</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1995</th>\n",
       "      <td>124500.30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1996</th>\n",
       "      <td>124821.36</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1997</th>\n",
       "      <td>135969.78</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "variables  Deuda externa acumulada, total (DOD, US$ a precios actuales)\n",
       "1993                                               117269.60           \n",
       "1994                                               112309.71           \n",
       "1995                                               124500.30           \n",
       "1996                                               124821.36           \n",
       "1997                                               135969.78           "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "root = 'Variables_economicas/deuda externa acumulada.csv'\n",
    "tipo_cambio_2(root)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>variables</th>\n",
       "      <th>Inversión extranjera directa, entrada neta de capital (balanza de pagos, US$ a precios actuales)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1993</th>\n",
       "      <td>3903.58</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1994</th>\n",
       "      <td>8807.63</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1995</th>\n",
       "      <td>7113.28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1996</th>\n",
       "      <td>7275.91</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1997</th>\n",
       "      <td>11720.02</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "variables  Inversión extranjera directa, entrada neta de capital (balanza de pagos, US$ a precios actuales)\n",
       "1993                                                 3903.58                                               \n",
       "1994                                                 8807.63                                               \n",
       "1995                                                 7113.28                                               \n",
       "1996                                                 7275.91                                               \n",
       "1997                                                11720.02                                               "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "root_2 = 'Variables_economicas/IED.csv'\n",
    "tipo_cambio_2(root_2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>variables</th>\n",
       "      <th>Exportaciones de mercaderías (US$ a precios actuales)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1993</th>\n",
       "      <td>46147.41</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1994</th>\n",
       "      <td>48869.98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1995</th>\n",
       "      <td>59394.01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1996</th>\n",
       "      <td>76041.60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1997</th>\n",
       "      <td>100878.72</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "variables  Exportaciones de mercaderías (US$ a precios actuales)\n",
       "1993                                                46147.41    \n",
       "1994                                                48869.98    \n",
       "1995                                                59394.01    \n",
       "1996                                                76041.60    \n",
       "1997                                               100878.72    "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "root = 'Variables_economicas/Exportaciones.csv'\n",
    "tipo_cambio_2(root)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
