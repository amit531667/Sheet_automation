import schedule
import time
import requests
import json
import urllib, json
import urllib.request, json
from urllib.request import Request, urlopen
import pandas as pd

import gspread
from oauth2client.service_account import ServiceAccountCredentials


def data_frame(url,array_key):
    headersParam = {
        "username": "amit.kumar@taskmo.com",
        "authorization": "Authorization: Basic YW1pdC5rdW1hckB0YXNrbW8uY29tOlRNYW1pdEAxOTk0"
    }

    url = url

    #try:
    request = Request(url, headers=headersParam)

    a = urlopen(request).read()
    b = json.loads(a.decode('utf-8'))
    from json_normalize import json_normalize
    df = pd.json_normalize(b, array_key)
    return df


def uncle_delivery():
    headersParam = {
        "username": "amit.kumar@taskmo.com",
        "authorization": "Authorization: Basic YW1pdC5rdW1hckB0YXNrbW8uY29tOlRNYW1pdEAxOTk0"
    }

    url = 'https://backdashboard.taskmo.in/excel/uncle_delivery'  # view API  360177297434

    request = Request(url, headers=headersParam)
        # print(request)
        # if response.status_code == '503':
        #   print('error.503')
        # else:
    a = urlopen(request).read()
    b = json.loads(a.decode('utf-8'))

    df = pd.json_normalize(b, 'sow')
    return df
def upload_to_sheet(data_frame,spreadsheet_key,wks_name):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    from df2gspread import df2gspread as d2g
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/mac/Desktop/py/service.json', scope)
    gc = gspread.authorize(credentials)
            #spreadsheet_key="1x9kzKciGXepm39SA5HlviY3_wK2wGDnQGHBR5bgEbjk"
    spreadsheet_key = spreadsheet_key
    wks_name = wks_name
    #print("checkk")
    d2g.upload(data_frame, spreadsheet_key, wks_name, credentials=credentials, row_names=False, clean=True)
    return "uploaded"
