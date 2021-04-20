from flask import Flask, render_template, request

import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open("df.pkl", 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender = request.form['Gender']
        if Gender == "Male":
            Gender = 1
        else:
            Gender = 0

        Race=request.form['Race/ethnicity']
        if(Race=='Group A'):
            Race = 0
        elif(Race=="Group B"):
            Race = 1 
        elif(Race=="Group C"):
            Race = 2
        elif(Race=="Group D"):
            Race= 3
        else:
            Race = 4
        
        Parental_Level_of_Education = request.form['Parental_Level_of_Education']
        if Parental_Level_of_Education == "some high school":
            Parental_Level_of_Education = 5
        elif Parental_Level_of_Education =="high school":
            Parental_Level_of_Education =4
        elif Parental_Level_of_Education =="associate's degree":
            Parental_Level_of_Education = 3
        elif Parental_Level_of_Education == "master's degree":
            Parental_Level_of_Education = 2
        elif Parental_Level_of_Education == "some college":
            Parental_Level_of_Education = 1
        else :
            Parental_Level_of_Education = 0 


        Math_score = int(request.form['Math_Score'])

        Reading_score = int(request.form['Reading_score'])

        Writing_score = int(request.form['Writing_score'])


        Lunch = request.form['Lunch']
        if(Lunch=="standard"):
            Lunch = 1
        else:
            Lunch = 0
        
        test_preparation_course = request.form['test_preparation_course']
        if test_preparation_course == "None":
            test_preparation_course = 1
        else:
            test_preparation_course = 0


      
        prediction=model.predict(([[Gender,Race,Parental_Level_of_Education,Math_score,Reading_score,Writing_score,Lunch,test_preparation_course]]))
        print(prediction)
        prediction=np.round(prediction[0],2)
        return render_template('index.html',Average=prediction)
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)