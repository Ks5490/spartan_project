from flask import Flask, jsonify, request
import json


app = Flask(__name__)


#### WORKING NEED TO ADD EXP OF API --- WILL DO IN HTML IF TIME TOWARDS END ####
@app.route("/", methods = ["GET"])
def home_page():
    return "Welcome to my first sparta project ---- This is how to use API's: XXXXXXXXXXXXXXXXXXXXXX"



##### WORKING ADDS EMPLOYEE TO JSON #####
@app.route("/spartan/add", methods = ['POST'])
def add_employee():
    employee_data_as_dict_for_json = {}
    employee_data = request.json
    First_name = employee_data["First Name"]
    Last_name = employee_data["Last Name"]
    employee_id = employee_data["Employee ID"]

    employee_data_as_dict_for_json[employee_id] = employee_data

    try:
        with open("spartan_data.json", "r+") as sparta_json:
            data_dict = json.load(sparta_json)
            data_dict.update(employee_data_as_dict_for_json)
            sparta_json.seek(0)
            json.dump(data_dict, sparta_json, indent=3)

    
        return data_dict
           
    except Exception as ex:
        print("There was an error")
        print(ex)


### Working with correct ID and without valid id ###
@app.route("/spartan/<spartan_id>", methods = ["GET"])
def show_spartan(spartan_id):
    spartan_id_str = str(spartan_id)

    if spartan_id_str in data_dict.keys():
        return data_dict[spartan_id_str]
    else:
        return f"There is no Employee with this ID : {spartan_id_str}"




#### COME BACK TO THIS POST NOT AUTHORISED ###
@app.route("/spartan/remove", methods = ["POST"])
def remove_employee():
    iden_variable = request.args.get("sparta_id")




    sparta_id_str = str(iden_variable)

    if sparta_id_str in data_dict.keys():
        del data_dict[sparta_id_str]
       

        try:
            with open("spartan_data.json", "w") as j:
                json.dump(data_dict, j, indent=9)

        except Exception as ex:
            return f"There was an {ex} error"

        return "Employee data successfully removed"         
    else:
        return "Cannot remove employee as There is no employee with this ID"

   


### Working with hardcoded json ###
@app.route("/spartan", methods = ["GET"])
def show_spartan_list_json():
    json_data = json.dumps(data_dict)
    return json_data




### Start of Main ###
if __name__ == "__main__":

    try:
        with open("spartan_data.json", "r+") as sparta_json:
           data_dict = json.load(sparta_json)
            
        app.run()

    except Exception as ex:
        print("There was an error")
        print(ex)
