from flask import Flask,render_template,request

import joblib

app=Flask(__name__)

model=joblib.load(
'model.pkl'
)

@app.route('/')

def home():

    return render_template(
    'index.html'
    )

@app.route('/predict',methods=['POST'])

def predict():

    month=int(
    request.form['month']
    )

    prediction=model.predict(
    [[month]]
    )

    result=round(
    prediction[0],
    2
    )

    return render_template(

    'index.html',

    prediction_text=

    f"Predicted Expense: ₹{result}"

    )

if __name__=="__main__":

    app.run(
    debug=True
    )