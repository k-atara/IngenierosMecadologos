from sklearn import tree
import pandas as pd
df = pd.read_excel('./dataset.xlsx')

column1 = {
    "nan": -1,
}
column2 = {
    
}



data_values = []
data_classes = []
for i in range(0, df.shape[0]):
    row = df.loc[0].values.tolist()
    data_values.append(row[1:-1])
    data_classes.append(row[-1])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(data_values, data_classes)

print("===============================================================")


result = clf.predict([[1.0, "nan", 'Piura', 'Piura', 'Veintiseis de Octubre', "nan", "nan", -5.163182, -80.682388, 'Vivienda Unifamiliar', "nan", "nan", 0.0, "nan", 'En construcción', 'Costos o reposición (directo)', '62.50', '27.58']])

print(result)








