from flask import Flask, jsonify, request
import json
import managment


app = Flask(__name__)


#### WORKING NEED TO ADD EXP OF API --- WILL DO IN HTML IF TIME TOWARDS END ####
@app.route("/", methods = ["GET"])
def home_page():
    return "Welcome to my first sparta project ---- This is how to use API's: XXXXXXXXXXXXXXXXXXXXXX"


#####  NEEDS VALIDATION OF INPUT - MAYBE CUSTOM ERROR / HTML #####
@app.route("/spartan/add", methods = ['POST'])
def additiion_of_employee_POST():
    return managment.add_employee()


### Working with correct ID and without valid id with external managment.py file ###
@app.route("/spartan/<spartan_id>", methods = ["GET"])
def show_spartan_page(spartan_id):
    return managment.show_spartan(spartan_id)


#### WORKING REMOVES EMPLOYEE FROM JSON FUNCTIONAL AND TESTED ###
@app.route("/spartan/remove", methods = ["POST"])
def remove_employee_POST():
    iden_variable = request.args.get("sparta_id")
    sparta_id_str = str(iden_variable)
    return managment.remove_employee(sparta_id_str)
        

### Working with hardcoded json and external managment.py file ###
@app.route("/spartan", methods = ["GET"])
def show_spartan_list_json_page():
    return managment.show_spartan_list_json()


### Start of Main ###
if __name__ == "__main__":
            
        app.run()

   