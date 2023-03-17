from flask import Flask,render_template,request,redirect
import pickle
import numpy as np

model=pickle.load(open("model.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict_admission():
    gre_score=float(request.form.get("gre_score"))
    tofel_score=float(request.form.get("tofel_score"))
    cgpa=float(request.form.get("cgpa"))
    result=model.predict(np.array([[gre_score,tofel_score,cgpa]]))
    return render_template('index.html', chance_of_admit='student has a probability to get admission  {}'.format(result))

    #if result>=0.8:
    #   return "<h1 style='color:green'>Admitted</h1>"
    #else:
     #  return "<h1 style='color:red'>NOT Admitted</h1>"
    
    
# @app.route("/predict",methods=["GET"])
# def predict_placement():
#     cgpa=float(request.args.get("cgpa"))
#     iq=float(request.args.get("iq"))
#     profile_score=float(request.args.get("profile_score"))
    
    
#     result=model.predict(np.array([[cgpa,iq,profile_score]]))
    
#     if result[0]==1:
#         return "<h1 style='color:green'>PLACED</h1>"
#     else:
#         return "<h1 style='color:red'>NOT PLACED</h1>"   


app.run(host="127.0.0.1",port=5001,debug=True)