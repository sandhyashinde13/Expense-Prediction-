import pandas as pd

from sklearn.linear_model import LinearRegression

import joblib

data = pd.read_csv(
"personal_expense_datasets.csv"
)

# Use first 400 rows only

data = data.head(400)

month_map={

'January':1,
'February':2,
'March':3,
'April':4,
'May':5,
'June':6,
'July':7,
'August':8,
'September':9,
'October':10,
'November':11,
'December':12

}

data['Month_Number']=data['Month'].map(
month_map
)

data=data.dropna()

X=data[['Month_Number']]

y=data['Amount']

model=LinearRegression()

model.fit(
X,
y
)

joblib.dump(
model,
'model.pkl'
)

print(
"Model Trained Successfully"
)