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
BOOKS = 'books!A:D'
POSTS = 'posts!A:C'

def main():
    # def __init__(self):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    book_fetch = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=BOOKS).execute()
    book_list = book_fetch.get('values', [])

    post_fetch = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=POSTS).execute()
    post_list = post_fetch.get('values', [])
    
    return [book_list, post_list]
    # return post_list

# def books():
#     return main.book_list
#
# def posts():
#     return main.post_list

# if __name__ == '__main__':
#     main()
