import requests
import os

def prepare_request_dict(dir_name :str)->list:
    final_list = []
    for name in os.listdir(dir_name):
        full_name = os.path.join(dir_name,name)
        if not os.path.isdir(full_name):
            file = open(full_name)
            lines = file.readlines()
            file.close()
            dict = {}
            dict.update({"title": lines[0].strip()})
            dict.update({"name": lines[1].strip()})
            dict.update({"date": lines[2].strip()})
            dict.update({"feedback":''.join(i for i in lines[3:])})
            final_list.append(dict)
    return final_list

dir_name = "feedback_dirc"
for i in prepare_request_dict(dir_name):
    response = requests.post("http://<corpweb-external-IP>/feedback",json = i)
    response.raise_for_status()
    print(response.status_code)
    print(response.text)
    response.request
    print("----------")

