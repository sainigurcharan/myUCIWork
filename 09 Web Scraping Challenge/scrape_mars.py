from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import time

# INITIALIZING SPLINTER
def init_browser():
    # MAC USERS
    # executablePath = {'executable_path': 'chromedriver.exe'}
    # return Browser('chrome', **executablePath, headless=False)

    # WINDOWS USERS
    executablePath = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', headless=True, **executablePath)

# DICTIONARY TO INCLUDE ALL THE SCRAPED DETAILS
marsInfo = {}

# NASA MARS NEWS
def MARSNews():

    try:
        # INITIALIZING SPLINTER
        browser = init_browser()

        # NASA NEWS SCRAPING WITH SPLINTER
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)
        time.sleep(1)
        html = browser.html

        soup = BeautifulSoup(html, 'html.parser')

        # SCRAPE NEWS TITLE AND PARAGRAPH
        news_title = soup.find('div', class_='content_title').find('a').text
        news_p = soup.find('div', class_='article_teaser_body').text

        print(news_title)
        print(news_p)

        marsInfo['news_title'] = news_title
        marsInfo['news_p'] = news_p
        return marsInfo

    finally:
        browser.quit()

# FEATURED IMAGE
def MARSImage():

    try:
        # INITIALIZING SPLINTER
        browser = init_browser()

        # MARS SPACE IMAGE SCRAPING WITH SPLINTER
        featuredImageJPL = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(featuredImageJPL)
        time.sleep(1)
        htmlImage = browser.html

        soup = BeautifulSoup(htmlImage, 'html.parser')

        # SCRAPE BACKGROUND IMAGE URL
        featuredImageURL = soup.find('article')['style']
        featuredImageURL = featuredImageURL.replace('background-image: url(', '').replace(');', '')[1:-1]
        featuredImageURL = 'https://www.jpl.nasa.gov' + featuredImageURL

        print(featuredImageURL)

        marsInfo['featured_image_url'] = featuredImageURL
        return marsInfo

    finally:
        browser.quit()

# MARS WEATHER
def MARSWeather():

    try:
        # INITIALIZING SPLINTER
        browser = init_browser()

        # MARS WEATHER SCRAPING WITH SPLINTER
        weatherURL = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(weatherURL)
        time.sleep(1)
        htmlWeather = browser.html

        soup = BeautifulSoup(htmlWeather, 'html.parser')

        # SCRAPING TOP WEATHER TWEET FROM LIST OF TWEETS
        latestTweets = soup.find_all('div', class_='js-tweet-text-container')
        for tweet in latestTweets:
            weatherTweet = tweet.find('p').text
            if 'Sol' and 'pressure' in weatherTweet:
                print(weatherTweet)
                break
            else:
                pass

        weatherTweet = weatherTweet.replace('InSight ', '')
        weatherTweet = weatherTweet[:weatherTweet.find('hPa') + 3]
        marsInfo['weather_tweet'] = weatherTweet
        return marsInfo

    finally:
        browser.quit()

# MARS FACTS
def MARSFacts():

    # MARS FACTS SCRAPING WITH SPLINTER
    factsURL = 'http://space-facts.com/mars/'
    marsFacts = pd.read_html(factsURL)
    marsDF = marsFacts[0]

    # CREATING DATAFRAME FROM SCRAPED NEWS
    marsDF.columns = ['Description', 'Value']
    marsDF.set_index('Description', inplace=True)
    data = marsDF.to_html()

    marsInfo['mars_facts'] = data
    return marsInfo

# MARS HEMISPHERES
def MARSHemisphere():

    try:
        # INITIALIZING SPLINTER
        browser = init_browser()

        # MARS HEMISPHERE SCRAPING WITH SPLINTER
        hemispheresURL = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemispheresURL)
        time.sleep(1)
        htmlHemispheres = browser.html
        hemisphereImageURLs = []

        soup = BeautifulSoup(htmlHemispheres, 'html.parser')
        allItems = soup.find_all('div', class_='item')

        hemispheresURL = 'https://astrogeology.usgs.gov'

        # SCRAPPING THE ALL IMAGE ITEMS
        for i in allItems:
            title = i.find('h3').text
            partialImgURL = i.find('a', class_='itemLink product-item')['href']

            # URL FOR EXACT IMAGE
            browser.visit(hemispheresURL + partialImgURL)
            time.sleep(1)
            partialImgHtml = browser.html
            soup = BeautifulSoup(partialImgHtml, 'html.parser')

            # SCRAPE THE IMAGE
            imgURL = hemispheresURL + soup.find('img', class_='wide-image')['src']
            hemisphereImageURLs.append({"title": title, "img_url": imgURL})

        marsInfo['hemisphereImageURLs'] = hemisphereImageURLs
        return marsInfo

    finally:
        browser.quit()