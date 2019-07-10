'''
Script for scraping all movie budget and box office data from 
The Numbers, cleaning it, and saving it to a CSV

Start page/reference: https://www.the-numbers.com/movie/budgets/all
'''

import requests
import pandas as pd
from bs4 import BeautifulSoup


#1. generates a list with all url endings needed for scraping
suffixes = ['']
for i in range(1, 58):
    suffixes.append('/' + str(i*100+1))


#2. scrapes raw data from web to list of lists
full_data_list = []

for i in range(len(suffixes)):
    suffix = suffixes[i]
    url = 'https://www.the-numbers.com/movie/budgets/all' + suffix
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    parsed_raw_data = soup.find_all('td')

    data_list = []
    for i in range(len(parsed_raw_data)):
            data_list.append(parsed_raw_data[i].get_text())
            if i != 0 and i % 6 == 0:
                full_data_list.append(data_list)
                data_list = []


#3. removing superfluous indices, which occur at jumps from one page to the next (makes conversion to dataframe much smoother)
for i in range(len(full_data_list)):
    if len(full_data_list[i]) == 7:
        del full_data_list[i][0]
    elif len(full_data_list[i]) > 7:
        print("Houston, we have a problem.")
    else:
        continue


#4. converting to pandas dataframe, cleaning
df = pd.DataFrame.from_records(full_data_list, columns=['release', 'title', 'budget', 'domestic', 'worldwide', 'idx'])

for col in ['budget', 'domestic', 'worldwide']:
    df[col] = df[col].str.replace(',', '')
    df[col] = df[col].str.replace('$', '')
    df[col] = df[col].astype(int)

df = df.drop(['idx'], axis=1)
df['release'] = pd.to_datetime(df['release'])
df['title'] = df['title'].astype('str')


#5. saving dataframe to csv
filepath = '../../data/raw/the-numbers.csv' #or insert path of your choice including file name, e.g. '/Users/yourname/Desktop/data.csv'
df.to_csv(filepath, index=False)

print(str(len(df)) + " films saved to csv.")
