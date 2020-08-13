# -*- coding: UTF-8 -*-

from __future__ import print_function
import yaml
import pickle
import os.path
import inspect
import json
import jsonpickle
import requests
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#lülitan välja automaatse YAML ankrute genereerimise
class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

totalcount = 0
sheets = []

os.chdir(os.path.dirname(__file__))



def authenticate():

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    print("authenticating")
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds


def connect(creds):
    print('connecting')
    service = build('sheets', 'v4', credentials=creds)
    return service


def fetchDataFromSheet(service, sheetName):
    print('\nfetching data from sheet: ' + sheetName)

    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1rZaQfVqVgdnJRLHwp02deUoISndpprC8ZQtxfK6zK-E'
    SAMPLE_RANGE_NAME = sheetName

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    return values


def createJSON(values, location):
    values2 = []
    for row in values[1:]:
        while len(row) < len(values[0]):
            row.append('')

        values2.append({'Code': row[0], 'Name': {'et': row[1],'en': row[2],'ru': row[3]}})

    with open(r'../source/' + location, 'w', encoding='utf-8') as file:
        json.dump(values2, file, indent=4)

    return values2


def postToStrapi(data):
    url = "http://139.59.130.149/languages"

    for item in data:
        payload = json.dumps(item)
        print(payload)
        headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNTk3MjQwNDA2LCJleHAiOjE1OTk4MzI0MDZ9.ZddzcDSe7O130sr4dtxr2XOSP7j-BTmlOI8TGxWgKdM',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data = payload)

        print(response.text.encode('utf8'))


def main(sheetName, location):
    if __name__ == '__main__':

        values = fetchDataFromSheet(service, sheetName)
        values2 = createJSON(values, location)
        postToStrapi(values2)

        global totalcount
        totalcount = totalcount + 1
        sheets.append(sheetName)


def authconnect():
    creds = authenticate()
    service = connect(creds)
    return service



def report():
    print('\nFetched ' + str(totalcount) + ' sheets:')

    for x in sheets:
        print(x)

    return len(sheets)



""" siin kutsun välja üleval defineeritud funtiooni andes kaasa parameetritena:
- sheetName = Google sheets lehekülje nimi kust infot loeme
- location = kuhu fail genereeritakse ja mis selle nimi on (nt 'asukoht/failiNimi.yaml')
- dataSources = dictionary tüüpi objekt lisatavatest failidest (nt {'pictures': '/film_pictures.yaml', 'screenings': 'screenings.yaml'})
    kui ei ole midagi vaja lisada  kirjuta {}
"""
"""
The issue with this is the use of aliases.
Basically since the data I had in the ‘services’ dictionary was the same as what
I had in parameters pyYAML recognized that and created the alias &id001 pointing at that data,
then referenced it rather than copying that data into parameters.

class MyDumper(yaml.Dumper):
def ignore_aliases(self, _data):
return True



"""

service = authconnect()

main('ISOlanguages', '../helpers/strapiLang.json')

x = report()


