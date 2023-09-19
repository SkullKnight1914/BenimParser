import requests
import json
import time
import os

#   Get list of previously created files with list of vacancies and go throught it in a loop
for file in os.listdir(r'C:\Users\bulat\PycharmProjects\PA\HHru_parsing\docs\pagination'):

    #   Open file, reading its contents and closing file
    file = open(r'C:\Users\bulat\PycharmProjects\PA\HHru_parsing\docs\pagination\{}'.format(file), encoding='utf-8')
    jsonText = file.read()
    file.close()

    #   Converting the received text in object dictionary
    jsonObj = json.loads(jsonText)

    #   Get and through it by vacancies list
    for vacancy in jsonObj['items']:

        #   We turn to API and get detailed info by specific vacancy
        req = requests.get(vacancy['url'])
        data = req.content.decode()
        req.close()

        #   Creating file in JSON format with id vacancy as name
        #   Writing in it response of request and closing file
        fileName = r'C:\Users\bulat\PycharmProjects\HHru_parsing\docs\vacancies\{}.json'.format(vacancy['id'])
        f = open(fileName, mode='w', encoding='utf-8')
        f.write(data)
        f.close()

        time.sleep(0.25)

print('Вакансии собраны')