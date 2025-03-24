import pandas as pd
import requests
import json
import os
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from datetime import datetime

#Create an HTML Session
session = HTMLSession()

#Define function

def collect_news(x1,x2):
    #intialize an empty list to hold the data
    dataframe = []

    #Create list of queries from funcion paramets
    queries = [x1,x2]

    #Loop through each query to gather news items
    for query in queries:
        url = f'https://news.google.com/rss/search?q={query}'
        response = session.get(url)
        if response.status_code != 200:
            raise Exception (f"HTTP Error: {response.status_code} - {response.reason}")

        #parse the RSS feed with BeautifulSoup
        soup = BeautifulSoup(response.content, 'xml')


        #Find all the RSS item elements
        press_items = soup.find_all('item')


        #Extract the information from the RSS feed
        for item in press_items:
            title = item.title.text if item.title else ''
            pub_date = item.pubDate.text if item.pubDate else ''
            description = item.description.text if item.description else ''
            source = item.source.text if item.source else ''
            link = item.link.text if item.link else ''

            #Append items to a dataframe
            dataframe.append({
                'title': title,
                'date': pub_date,
                'description': description,
                'source': source,
                'link': link
                })

            #Stop if we've collected 1000 items
            if len(dataframe) >= 1000:
                break

    return pd.DataFrame(dataframe)     

# Call the function and pass the news_data list
news_data = collect_news('kamala', 'trump')
news_data2 = collect_news('democrat', 'republican')
news_data3 = collect_news('student loan', 'economy')
news_data4 = collect_news('millennial voter', 'gen z voter')
news_data5 = collect_news('abortion', 'gun rights')
news_data6 = collect_news('JD Vance', 'Tim Waltz')
news_data7 = collect_news('Wall Street', 'Tech')
news_data8 = collect_news('post-dobbs', 'post-roe')
news_data9 = collect_news('pregnancy criminalization', 'pregnant women')
news_data10 = collect_news('pregnancy justice', 'pro-life')

#Concatenate all collected data into a dataframe
news_df = pd.concat([news_data, news_data2, news_data3, news_data4, news_data5, news_data6, news_data7, news_data8, news_data9, news_data10])

#Get today's date in YYYY-MM-DD format
today = datetime.today().strftime('%Y-%m-%d')

#Create the full path and filename with today's date
save_path = '/Users/lawhea1214/Documents/Udacity/Data_Analysis/Political_News_2024/political_news_data'
filename = os.path.join(save_path, f'political_news_data_{today}.csv')

#Save the DataFrame to CSV
news_df.to_csv(filename, index=False)

print(f"News saved to {filename}")


