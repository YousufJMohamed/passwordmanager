from flask import Flask, render_template,request
from flask_pymongo import PyMongo
from decouple import config

app = Flask(__name__)
app.config['MONGO_URI'] = config("MONGO_URI")
mongo            = PyMongo(app)
Password_manager = mongo.db.table

@app.route('/',methods=["POST","GET"])
def hello_world():
    return render_template("firstpage.html", title="Password_manager")



@app.route('/index',methods=["POST","GET"])
def hello():
    return render_template("index.html", title="enter details")

@app.route('/retrive',methods=['POST','GET'])
def retrive_details():
    return render_template("retrive.html",title="retrive page")

@app.route('/add-account-details',methods=["POST","GET"])
def add_details():
    data = {
            "Account name" : request.values.get("Account name"),
            "User Id" : request.values.get("User Id"),
            "Password" : request.values.get("Password")
            

    }
    print(data)
    Password_manager.insert_one(data)


    return render_template("added.html",title="account added")


@app.route('/get-account-details',methods=['GET','POST'])
def get_details():
    Account_name = request.values.get("Account name")
    results=Password_manager.find({"Account name":Account_name})
    return render_template("display.html",details=results)

   

if __name__=="__main__":
    app.run(debug=True)
