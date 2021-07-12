{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def tipo_cambio_2(root):\n",
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
