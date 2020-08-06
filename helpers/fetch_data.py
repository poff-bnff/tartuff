from __future__ import print_function
import yaml
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

os.chdir(os.path.dirname(__file__))

def fetchData(sheetName, location, dataSources):


    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1J_cYJnZI41V8TGuOa8GVDjnHSD9qRmgKTJR3sd9Ff7Y'
    SAMPLE_RANGE_NAME = sheetName

    def main():
        """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """
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

        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        # Check if any values found
        if not values:
            print('No data found.')
        else:
            print('Fetching ' + sheetName)
            # Counter
            count = 0
            dict_file = []
            headers = []
            nullkoht = None
            for row in values:
                if count == 0:
                    for x in row:
                        headers.append(x)
                else:
                    if row[0]:
                        count2 = 0
                        data = {}
                        for x in row:
                            if count2 == 0 and bool(dataSources) == True:
                                data['data'] = dataSources
                            data[headers[count2]] = row[count2].strip()
                            count2 = count2 + 1
                        dict_file = dict_file + [data]
                        with open(r'../source/' + location, 'w', encoding='utf-8') as file:
                            yaml.dump(dict_file, file, default_flow_style=False, sort_keys=False, indent=4, allow_unicode=True)
                count = count + 1
    if __name__ == '__main__':
        main()
""" siin kutsun välja üleval defineeritud funtiooni andes kaasa parameetritena:
- sheetName = Google sheets lehekülje nimi kust infot loeme
- location = kuhu fail genereeritakse ja mis selle nimi on (nt 'asukoht/failiNimi.yaml')
- dataSources = dictionary tüüpi objekt lisatavatest failidest (nt {'pictures': '/film_pictures.yaml', 'screenings': 'screenings.yaml'})
    kui ei ole midagi vaja lisada  kirjuta {}
"""
#fetchData('Artiklid', 'article/data.yaml', {'article_pictures': '/article_pictures.yaml'})
#fetchData('art-et', 'article/data_et.yaml', {'article_pictures': '/article_pictures.yaml'})
#fetchData('art-en', 'article/data_en.yaml', {'article_pictures': '/article_pictures.yaml'})
#fetchData('art-ru', 'article/data_ru.yaml', {'article_pictures': '/article_pictures.yaml'})

#fetchData('Events', 'events/data.yaml', {})
#fetchData('events-et', 'events/data_et.yaml', {})
#fetchData('events-en', 'events/data_en.yaml', {})
#fetchData('events-ru', 'events/data_ru.yaml', {})

#fetchData('Filmid', 'film/data.yaml', {'pictures': '/film_pictures.yaml', 'screenings': 'screenings.yaml'})
#fetchData('filmid-et', 'film/data_et.yaml', {'pictures': '/film_pictures.yaml', 'screenings': 'screenings.yaml'})
#fetchData('filmid-en', 'film/data_en.yaml', {'pictures': '/film_pictures.yaml', 'screenings': 'screenings.yaml'})
#fetchData('filmid-ru', 'film/data_ru.yaml', {'pictures': '/film_pictures.yaml', 'screenings': 'screenings.yaml'})

#fetchData('Seansid', 'film/screenings.yaml', {})
#fetchData('seansid-et', 'film/screenings_et.yaml', {})
#fetchData('seansid-en', 'film/screenings_en.yaml', {})
#fetchData('seansid-ru', 'film/screenings_ru.yaml', {})


