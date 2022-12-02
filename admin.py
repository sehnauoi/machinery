# gunakan modul json
import json
from datetime import datetime
import pytz
import os


date = datetime.now(pytz.timezone('Etc/GMT-11')).strftime('%Y-%m-%d')
json_files = open('/workspaces/machinery/laundry/datas/member.json')

def new_member():
    name = input("masukan nama member baru")

    def write_json(new_data, filename = '/workspaces/machinery/laundry/datas/member.json'):
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            file_data.append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)

        # print("data succesfully added", new_data)
    
    new_data = {
        "name":name.lower(),
        "date":date
        }
        
    write_json(new_data)

def read_member():
    x =  json_files
    data = json.load(x)
    w = []
    for x in data:
        # print(x)
        w.append(x)
    
    return w

def look_member(name):
    datas = []
    datas.clear()
    try:
        name = name.lower()
        data = read_member()
        for x in data:
            if x['name'] == name:
                datas.clear()
                datas.append(x['name'])
                datas.append(x['date'])
                break

            else:
                datas.clear()
                datas.append(name)
                datas.append(date)
                continue
        
        name = datas[0]
        mdate = datas[1]

        # print(datas)
        return name, mdate
    
    except ValueError:
        return name, date

def view_data():# Prints JSON Array to screen
    x = json_files
    data = json.load(x)
    i = 0
    for item in data:
        
        name = item["name"]
        datex = item["date"]

        print(f"Index Number: {i}")
        print(f"Name : {name}")
        print(f"Date registered : {datex}")
        print("\n")
        i = i + 1

def delete_data():    # Deletes an element from the array
    view_data()
    new_data = []

    with open("/workspaces/machinery/laundry/datas/member.json", "r") as f:
        temp = json.load(f)

        data_length = len(temp) - 1
    print("Pilih index yang akan dihapus")
    delete_option = input(f"Pilih index 0-{data_length} : ")
    i=0

    for entry in temp:
        if i == int(delete_option):
            pass
            i = i + 1
        else:
            new_data.append(entry)
            i= i + 1

    with open("/workspaces/machinery/laundry/datas/member.json", "w") as f:
        json.dump(new_data, f, indent=4)
    print("data terhapus\n")

def save_data(name, weight, income):
    try:
        def write_json(new_data, filename = '/workspaces/machinery/laundry/datas/transaction.json'):
            with open(filename, 'r+') as file:
                file_data = json.load(file)
                file_data.append(new_data)
                file.seek(0)
                json.dump(file_data, file, indent = 4)

            # print("data succesfully added", new_data)
        
        new_data = {
            "date" : date,
            "name" : name,
            "weight" : weight,
            "income" : income
            }    
        
        write_json(new_data)
        print("*data berhasil disimpan")
    
    except ValueError:
        print("Program error")
