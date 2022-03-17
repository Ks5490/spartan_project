import json
from flask import Flask, request
from idna import valid_contextj
from spartan import Spartan


def add_employee():
    employee_data_as_dict_for_json = {}

    ### Reading in User input (POST)
    employee_data = request.json
    First_name = employee_data["First Name"]
    Last_name = employee_data["Last Name"]
    employee_id = employee_data["Employee ID"]
    birth_year = employee_data["Birth Year"]
    birth_month = employee_data["Birth Month"]
    birth_day = employee_data["Birth Day"]
    course = employee_data["Course"]
    stream = employee_data["Stream"]


    ### Validation of User input ###
    validation_first_name = Spartan.first_last_name_validation(First_name)
    if validation_first_name != "v":
        return "Failed First Name Validation - Must contain minimum of 2 characters"

    validation_last_name = Spartan.first_last_name_validation(Last_name)
    if validation_last_name != "v":
        return "Failed Last Name Validation - Must contain minimum of 2 characters"

    validation_year_of_birth = Spartan.year_validation(birth_year)
    if validation_year_of_birth != "v":
        return "Failed Year of Birth Validation - Must be an integer between 1900 - 2004"

    validation_month_of_birth = Spartan.month_validation(birth_month)
    if validation_month_of_birth != "v":
        return "Failed Month of Birth Validation - Must be an integer between 1 - 12"

    validation_day_of_birth = Spartan.day_validation(birth_day)
    if validation_day_of_birth != "v":
        return "Failed Day of Birth Validation - Must be an integer between 1 - 31"

    validation_course = Spartan.stream_course_validation(course)
    if validation_course != "v":
        return "Failed Course Validation - Must be a non empty string"

    validation_stream = Spartan.stream_course_validation(stream)
    if validation_stream != "v":
        return "Failed Stream Validation - Must be a non empty string"
    

    ### Taken ID Validation ###
    try:
        with open("spartan_data.json", "r+") as sparta_json:
            data_dict = json.load(sparta_json)
           
        if employee_id in data_dict.keys():
            return "The selected ID is taken - please try different ID or examine Spartan Data to check ID availibility"

    except Exception as ex:
        return f"There was an error: {ex}"


    ### Adding validated user input (POST) into json file database ###
    employee_data_as_dict_for_json[employee_id] = employee_data

    try:
        with open("spartan_data.json", "r+") as sparta_json:
            data_dict = json.load(sparta_json)
            data_dict.update(employee_data_as_dict_for_json)
            sparta_json.seek(0)
            json.dump(data_dict, sparta_json, indent=3)
            return f"Employee {First_name} {Last_name} added to the database"
           
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