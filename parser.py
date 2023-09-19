#   Library for working with HTTP requests. We will using this for access to API
import requests
#   Package for convenient working with data in JSON format
import json
#   Module for working with values time
import time
#   Module for working with OS, we will using for working with files
import os

def getPage(page = 0):
    """Creating method for getting page with vacancies list"""

    # Dictionary for GET-request
    params = {
        'text' : 'NAME:DevOps', # filter text
        'area' : 1, # for Moscow valid "1" value
        'page' : page, # page index
        'per_page' : 100 # Numbers of vacancies on 1 page
    }

    req = requests.get('https://api.hh.ru/vacancies', params) # Sending request to API
    data = req.content.decode() # Decoding his response, so that cyrillic alphabet displayed correctly
    req.close()
    return data


#   Reading first 2000 vacancies. HH API can't give more than 2000 vacancies
for page in range(0,20):

    # Converting text of the response request in Python dictionary
    jsObj = json.loads(getPage(page))

    # Saving files in directory .\docs\pagination
    # Determine numbers of files in directory for saving document with response request
    # The resulting value is used to form the name of the document
    nextFileName = r'C:\Users\bulat\PycharmProjects\HHru_parsing\docs\pagination\{}.json'.format(len(os.listdir(r'C:\Users\bulat\PycharmProjects\PA\HHru_parsing\docs\pagination')))

    # Creating new document, writing response of request there and closing
    file = open(nextFileName, mode='w', encoding='utf-8')
    file.write(json.dumps(jsObj, ensure_ascii=False))
    file.close()

    # Checking on the last page, if vacancies less than 2000
    if (jsObj['pages'] - page) <= 1:
        break

    # Delay
    time.sleep(0.25)

print('Страницы поиска собраны')