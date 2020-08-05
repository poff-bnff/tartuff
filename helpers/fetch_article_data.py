from __future__ import print_function
import yaml
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

os.chdir(os.path.dirname(__file__))

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1J_cYJnZI41V8TGuOa8GVDjnHSD9qRmgKTJR3sd9Ff7Y'
SAMPLE_RANGE_NAME = 'Artiklid'

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
        print('Fetching articles')

        # Counter
        count = 0

        #
        dict_file = []
        headers = []

        for row in values:

            if count == 0:
                for x in row:
                    headers.append(x)

            else:
                if row[0]:
                    count2 = 0
                    data = {}
                    for x in row:

                        if count2 == 0:
                            data['data'] = {'article_pictures': '/article_pictures.yaml'}

                        data[headers[count2]] = row[count2].strip()

                        count2 = count2 + 1

                    dict_file = dict_file + [data]

                    with open(r'../source/article/data.yaml', 'w', encoding='utf-8') as file:
                        yaml.dump(dict_file, file, default_flow_style=False, sort_keys=False, indent=4, allow_unicode=True)

            count = count + 1


if __name__ == '__main__':
    main()

