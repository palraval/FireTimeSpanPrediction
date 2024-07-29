from flask import Flask, render_template, url_for, request
import pickle
import pandas as pd


app = Flask(__name__)

with open('choices.pkl', 'rb') as f:
    choices = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('encode_data.pkl', 'rb') as f:
    encoded_data = pickle.load(f)


cat_cols = [col for col in choices.keys() if choices[col] != None]
cont_cols = [col for col in choices.keys() if choices[col] == None]


@app.route("/", methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        input_data = request.form.to_dict()
        result = predict(input_data)
        styles = url_for('static', filename = 'style.css')
        return render_template('index.html', styles_url = styles, choices = choices, result = result)
    
    else:
        return render_template('index.html', choices = choices)

def predict(input_data):
    input_df = pd.DataFrame([input_data])
    X = input_df[['incident_acres_burned','incident_longitude','incident_latitude','mean_temperature','Population',
                  'month_extinguished']].astype('float')
    X = pd.get_dummies(X)
    all_cols = encoded_data.columns
    X = X.reindex(columns=all_cols, fill_value=False)
    X_transform = scaler.transform(X)
    output = model.predict(X_transform)
    return int(output[0])



if __name__  == "__main__":
    app.run(debug = True)