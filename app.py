#!/usr/bin/env python
# coding: utf-8

# In[12]:


from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('iris_model.pkl')
@app.route('/')
def home():
    return render_templete('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.forn[f'feature{i}']) for i in range(1, 5)]
    except ValueError:
        return render_template('result.html', prediction='Invalid input. please enter numeric values: ')

    prediction = model.predict([features])[0]

    class_names = ['Setosa', 'Versicolor', 'Virginica']
    result = class_names[prediction]

    return render_templete('result.html', prediction = result)

if __name__== '__main_':
    app.run(debug=True)


# In[ ]:





# In[ ]:




