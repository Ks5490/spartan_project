from flask import Flask, jsonify, request
import json
import managment


app = Flask(__name__)


### Home page route ###
@app.route("/", methods = ["GET"])
def home_page():
    return "Welcome to my first sparta project ---- This is how to use API's: XXXXXXXXXXXXXXXXXXXXXX"


### Adding employee route (POST) ###
@app.route("/spartan/add", methods = ['POST'])
def additiion_of_employee_POST():
    return managment.add_employee()


### Displays specifc Spartan Data ###
@app.route("/spartan/<spartan_id>", methods = ["GET"])
def show_spartan_page(spartan_id):
    return managment.show_spartan(spartan_id)


### Removes specifc Spartan Data ###
@app.route("/spartan/remove", methods = ["POST"])
def remove_employee_POST():
    iden_variable = request.args.get("sparta_id")
    sparta_id_str = str(iden_variable)
    return managment.remove_employee(sparta_id_str)
        

### Displays all Spartan Data ###
@app.route("/spartan", methods = ["GET"])
def show_spartan_list_json_page():
    return managment.show_spartan_list_json()


### Start of Main ###
if __name__ == "__main__":
            
        app.run()

   