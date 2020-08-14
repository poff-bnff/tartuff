# -*- coding: UTF-8 -*-

from __future__ import print_function
import yaml
import pickle
import os.path
import inspect
import json
import jsonpickle
import requests
import pprint
pp = pprint.PrettyPrinter(indent=4).pprint


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
    SAMPLE_SPREADSHEET_ID = '1J_cYJnZI41V8TGuOa8GVDjnHSD9qRmgKTJR3sd9Ff7Y'
    SAMPLE_RANGE_NAME = sheetName

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    return values

def readJson(fileName):
    with open(r''+ fileName, encoding='utf-8') as f:
        data = json.load(f)
    return data

readJson('strapiFilms.json')

def splitCast(txt):
    names = txt.split(', ')
    cast = []
    for name in names:
        cast.append({'et':name, 'en':name, 'ru':name})
    return cast

def splitCompany(txt):
    names = txt.split(' / ')
    cast = []
    for name in names:
        cast.append({'et':name, 'en':name, 'ru':name})
    return cast

def splitCountriesLang(txt):
    countries = txt.split(', ')
    country = ''
    countryFromISOcountries = readJson('strapiFilms.json')
    for name in countries:
        for value in countryFromISOcountries:
            if name == value['Value_en']
                country == value['Code']
    return country

def createJSON(rows, location):
    filmList = []
    header = rows[0]
    for row in rows[1:]:
        while len(row) < len(rows[0]):
            row.append('')


        filmList.append({'FilmId': row[header.index('filmEventivalId')],
                        'Title_et': row[header.index('filmTitle_et')],
                        'Title_en': row[header.index('filmTitle_en')],
                        'Title_ru': '',
                        'TitleOriginal': row[header.index('filmTitleOriginal')],
                        # 'Countries': splitCountriesLang(row[header.index('filmCountries_en')])
                        'Year': row[header.index('filmYear')],
                        'Runtime': row[header.index('filmDuration')],
                        'Credentials': [{'Director': splitCast(row[header.index('filmCast')]),
                                        'Screenwriter': splitCast(row[header.index('filmScreenwriter')]),
                                        'DoP': splitCast(row[header.index('filmDop')]),
                                        'Cast': splitCast(row[header.index('filmCast')]),
                                        'Composer': splitCast(row[header.index('filmComposer')]),
                                        'Editor': '',
                                        'Producer': '',
                                        'CoProducer': '',
                                        'ProductionCompany': splitCompany(row[header.index('filmProduction')])
                                        }],
                        'Synopsis': [{'et': row[header.index('filmSynopsis_et')],
                                        'en': row[header.index('filmSynopsis_en')],
                                        'ru': ''}],
                        'Media': [{'Stills': '',
                                    'Posters': ''}],
                        'Trailer': row[header.index('filmTrailer')],
                        'QaClip': row[header.index('filmQaClip')],
                        'Tags': [{'Tag_premiere_types': '',
                                    'Tag_programmes': splitCast(row[header.index('tagProgramme')]),
                                    'Tag_genres': splitCast(row[header.index('tagGenre')]),
                                    'Tag_keywords': splitCast(row[header.index('tagKeyword')])
                                    }],
                        'Slug_et': row[header.index('path_et')],
                        'Slug_en': row[header.index('path_en')],
                        'Slug_ru': ''
                       })


    with open(r'../source/' + location, 'w', encoding='utf-8') as file:
        json.dump(filmList, file, indent=4)
    # pp(filmList)
    return filmList


# def postToStrapi(data):
#     url = "http://139.59.130.149/FILMS"

#     for item in data:
#         payload = json.dumps(item)
#         print(payload)
#         headers = {
#         'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNTk3MjQwNDA2LCJleHAiOjE1OTk4MzI0MDZ9.ZddzcDSe7O130sr4dtxr2XOSP7j-BTmlOI8TGxWgKdM',
#         'Content-Type': 'application/json'
#         }

#         response = requests.request("POST", url, headers=headers, data = payload)

#         print(response.text.encode('utf8'))


def main(sheetName, location):
    if __name__ == '__main__':

        values = fetchDataFromSheet(service, sheetName)
        filmList = createJSON(values, location)
        # postToStrapi(filmList)

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

main('Filmid', '../helpers/strapiFilms.json')

x = report()


