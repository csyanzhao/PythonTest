#coding=utf-8
import os
import sys
from aip import AipOcr
from PIL import Image
import base64
import json
import matplotlib.pyplot as plt
""" 你的 APPID AK SK """
APP_ID = '15439985'
API_KEY = 'jye3CogIQpOFY9V4OjLu4rvA'
SECRET_KEY = '20dNOCfrOPCu0pps7Fk7I2vw9ifeGrMX'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
#img=Image.open('C:\\1.jpg')
#img.show()
image = get_file_content('C:\\1.jpg')
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
#image = base64.b64encode(get_file_content('C:\\1.jpg'))
#print(image)
test = client.basicAccurate(image, options)
print(test)
#print((json.dumps(test, sort_keys=True, indent=4, separators=(',', ': '))))