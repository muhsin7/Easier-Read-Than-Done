from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1pALxHB4wUkwj6lRul1IccU9btgEETunz2jAyTElbObs'
BOOKS = 'Sheet1!A1:C2'
POSTS = 'Sheet2!A1:B2'

class main():

    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # # If there are no (valid) credentials available, let the user log in.
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             'credentials.json', SCOPES)
    #         creds = flow.run_local_server(port=0)
    #     # Save the credentials for the next run
    #     with open('token.pickle', 'wb') as token:
    #         pickle.dump(creds, token)

    # service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    # service = build('sheets', 'v4', credentials=creds)
    # sheet = service.spreadsheets()



    # TODO: DRY the code
    # def books():

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    book_fetch = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=BOOKS).execute()
    book_list = book_fetch.get('values', [])


    # def __init__(self, )
    print(book_list)
    #
    # def posts():
    #     service = build('sheets', 'v4', credentials=creds)
    #     sheet = service.spreadsheets()
    #     post_fetch = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
    #                                 range=POSTS).execute()
    #     post_list = post_fetch.get('values', [])
    #     return post_list

    # if not values:
    #     print('No data found.')
    # else:
    #     print('Name, Major:')
    #     for row in values:
    #         # Print columns A and E, which correspond to indices 0 and 4.
    #         print('%s, %s' % (row[0], row[4]))
    # print(values)

if __name__ == '__main__':
    main()
