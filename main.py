import gspread
from twitter import *

consumer_key = ''
consumer_secret = ''
token = ''
token_secret = ''

t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

    
gc = gspread.service_account('credentials.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("valley-of-tweets").sheet1

# Update a range of cells using the top left corner address

next_tweet = wks.acell('A1').value

# post a tweet throught the twitter API

t.statuses.update(
    status=next_tweet)
# delete a row on success posting
wks.delete_rows(2)