from flask import Flask,jsonify,render_template,request
import json
import config
from utils import risklevel

app = Flask(__name__)

@app.route("/")
def get_home():
    return("Welcome to the Maternal Health Risk Detection Interface")

@app.route("/risklevel",methods=["POST"])
def get_Risk_Level_status():
    if request.method=="POST":
        print("We are using GET method")
        data = request.form 
        print("Data from GET method",data)

        Age         =   data["Age"]
        SystolicBP  =   data["SystolicBP"]
        DiastolicBP =   data["DiastolicBP"]
        BS          =   data["BS"]
        BodyTemp    =   data["BodyTemp"]
        HeartRate   =   data["HeartRate"]
        

        risk_obj = risklevel(Age,SystolicBP,DiastolicBP,BS,BodyTemp,HeartRate)
        final_pred = risk_obj.get_Risk_Level_status()
        return jsonify({"Result":f"Predicted Maternal Health Risk Level status : {final_pred}"})
    
        
if __name__=="__main__":
    app.run(port=config.PORT_NUMBER_1,debug=False)
