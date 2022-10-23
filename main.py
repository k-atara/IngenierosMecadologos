import pandas as pd
import numpy as np
from unidecode import unidecode
import math
import sys
import time
to_drop = ["Fecha entrega del Informe", "Piso", "Posición", "Número de estacionamiento", "Número de frentes", "Elevador"]
df1 = pd.DataFrame(pd.read_excel('./dataset_formatted.xlsx'))
frames = [df1, df1.copy(), df1.copy(), df1.copy() ]
df1 = pd.concat(frames)
df2 = pd.DataFrame(pd.read_excel('./dataset.xlsx')).drop(to_drop, axis='columns')
df3 = df1.drop( to_drop , axis='columns')
nan_value = 0

def makeDict(input_list):
    temp_dict = dict({"nan": nan_value})
    index = 1
    for value in input_list:
        if type(value) is int or type(value) is float:
            if(math.isnan(value)):
                temp_dict["nan"] = nan_value
            else:
                return input_list
        elif value == "nan" or value == "NaN":
            temp_dict[unidecode(value).lower()] = nan_value
        else:
            temp_dict[unidecode(value).lower()] = index
            index = index + 1
        
    return temp_dict

def formatValues(input_list, values_in_dict):
    for index, value in enumerate(input_list):
        value = unidecode(str(value)).lower()
        if value in values_in_dict:
            input_list[index] = values_in_dict[value]
        else:
            if isinstance(value, str):
                if value.isdigit():
                    input_list[index] = int(value)
                else:
                    try:
                        if time.strptime(value, "%Y-%m-%d %H:%M:%S"):
                            input_list[index] = value
                            continue
                    except Exception as e:
                        # print(e)
                        pass
                    input_list[index] = float(value)
                      
                    
            else:
                input_list[index] = value
    return input_list

input = None
input_df = pd.DataFrame() 
original_df = pd.DataFrame() 
if len(sys.argv) == 2:
    print(f"File routine, trying to open: {sys.argv[1]}")
    to_drop.append('ID')
    to_drop.append('Valor comercial (USD)')
    input = pd.DataFrame(pd.read_excel(sys.argv[1]))
    print(input)
    original_df = input
    input = input.drop(to_drop,axis='columns')
    for header in (input):
        value = input.loc[:,header]
        values_in_dict = makeDict(value)
        # print(f"result dict -> {values_in_dict}")
        values_formatted = formatValues(value, values_in_dict)
        input_df[header] = values_formatted
elif len(sys.argv) > 2:
    print("Usage:")
    print("python <name_file> <file_to_read>.csv")
    exit()
else: 
    input = [{
        "Fecha entrega del Informe": "",
        "Tipo de vía": 0,
        "Piso":"",
        "Departamento": "lima",
        "Provincia": "lima", 
        "Distrito":"miraflores",
        "Número de estacionamiento":3,
        "Depósitos": 0, 
        "Latitud (Decimal)":-12.1105034, 
        "Longitud (Decimal)":-77.0455251, 
        "Categoría del bien":"departamento", 
        "Posición":"", 
        "Número de frentes":"", 
        "Edad":2, 
        "Elevador":1, 
        "Estado de conservación":"muy bueno",
        "Método Representado":"comparacion de mercado (directo)", 
        "Área Terreno":100, 
        "Área Construcción":227,
        "dormitorio":3
    },
    {
        "Fecha entrega del Informe": "",
        "Tipo de vía": 2,
        "Piso":"",
        "Departamento": "lima",
        "Provincia": "lima", 
        "Distrito":"miraflores",
        "Número de estacionamiento":3,
        "Depósitos": 0, 
        "Latitud (Decimal)":-12.1105034, 
        "Longitud (Decimal)":-77.0455251, 
        "Categoría del bien":"departamento", 
        "Posición":"", 
        "Número de frentes":"", 
        "Edad":2, 
        "Elevador":1, 
        "Estado de conservación":"muy bueno",
        "Método Representado":"comparacion de mercado (directo)", 
        "Área Terreno":100, 
        "Área Construcción":227,
        "dormitorio":3
    }
    ]


    for input_ind in input:
        for header in (df2.columns.values.tolist())[:-1]:
            value = [item[header] for item in input]
            values_in_dict = makeDict(value)
            # print(f"result dict -> {values_in_dict}")
            values_formatted = formatValues(value, values_in_dict)
            input_df[header] = values_formatted




for header in (df3.columns.values.tolist()):
  check_nan = df3[header].isnull().values.any()
  if check_nan:
    df3[header] = df3[header].fillna(nan_value)
    
print(input_df)


X = df3.drop('Valor comercial (USD)',axis='columns')
# print(X.head())

y = df3.loc[:,'Valor comercial (USD)']
# print(y.head())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.02,random_state=10)


from sklearn.ensemble import HistGradientBoostingRegressor
est = HistGradientBoostingRegressor()
est.fit(X_train, y_train)
score = est.score(X_test, y_test)


#save the model
import pickle
filename = './model/IngenierosMercadologosML.sav'
pickle.dump(est, open(filename, 'wb'))


predict = [round(item) for item in est.predict(input_df).tolist()] 
real_data = y_test.tolist()
print(f"predict   {(predict)}")
# print(f"real_data {(real_data)}")
print(f"score from test_set: {score}")
original_df["Valor comercial (USD)"] = predict
pd.to_datetime(original_df.loc[:,"Fecha entrega del Informe"], format="%Y-%m-%d %H:%M:%S")
from pathlib import Path  
filepath = Path('./out.xlsx')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
original_df.to_excel(filepath, index=False,encoding='utf-8-sig') 
# print(original_df)
