import json
from flask import Flask, request
from spartan import Spartan


def add_employee():
    employee_data_as_dict_for_json = {}
    employee_data = request.json

    First_name = employee_data["First Name"]
    Last_name = employee_data["Last Name"]
    employee_id = employee_data["Employee ID"]
    birth_year = employee_data["Birth Year"]
    birth_month = employee_data["Birth Month"]
    birth_day = employee_data["Birth Day"]
    course = employee_data["Course"]
    stream = employee_data["Stream"]

    employee_data_as_dict_for_json[employee_id] = employee_data

    try:
        with open("spartan_data.json", "r+") as sparta_json:
            data_dict = json.load(sparta_json)
            data_dict.update(employee_data_as_dict_for_json)
            sparta_json.seek(0)
            json.dump(data_dict, sparta_json, indent=3)
  
            return f"Employee {First_name} {Last_name} will be added to the database"
           
    except Exception as ex:
        return f"There was an error: {ex}"





#### Functional and tested within main ###
def show_spartan(spartan_id):
    spartan_id_str = str(spartan_id)
    try:
        with open("spartan_data.json", "r+") as sparta_json:
            data_dict = json.load(sparta_json)


        if spartan_id_str in data_dict.keys():
            return data_dict[spartan_id_str]
        else:
            return f"There is no Employee with this ID : {spartan_id_str}"

    except Exception as ex:
        return f"There was an error: {ex}"


def remove_employee(sparta_id_str):

    try:
        with open("spartan_data.json", "r+") as sparta_json:
            data_dict = json.load(sparta_json)
            if sparta_id_str in data_dict.keys():

                data_dict.pop(sparta_id_str)
               
                with open("spartan_data.json", "w") as sparta_json:
                        json.dump(data_dict, sparta_json, indent=3)

                return f"Employee with ID: {sparta_id_str} removed from database"   
            
            else:
                return "Cannot remove employee as There is no employee with this ID"

    except Exception as ex:
        return f"There was an error: {ex}"


def show_spartan_list_json():
    try:
        with open("spartan_data.json", "r+") as sparta_json:
            data_dict = json.load(sparta_json)
            return data_dict

    except Exception as ex:
        return f"There was an error: {ex}"