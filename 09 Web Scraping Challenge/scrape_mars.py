from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import time


# Initialize browser
def init_browser():
    # Mac Users
    # executablePath = {'executable_path': 'chromedriver.exe'}
    # return Browser('chrome', **executablePath, headless=False)

    # Windows Users
    executablePath = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', headless=True, **executablePath)

# Create Mission to Mars global dictionary
mars_info = {}

# NASA MARS NEWS
def MARSNews():
    try:
        # Initialize browser
        browser = init_browser()

        # Visit Nasa news url through splinter module
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)
        time.sleep(1)
        html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve the latest element that contains news title and news_paragraph
        news_title = soup.find('div', class_='content_title').find('a').text
        news_p = soup.find('div', class_='article_teaser_body').text

        # Display scrapped data
        print(news_title)
        print(news_p)

        # Dictionary entry from MARS NEWS
        mars_info['news_title'] = news_title
        mars_info['news_p'] = news_p
        return mars_info

    finally:

        browser.quit()


# FEATURED IMAGE
def MARSImage():
    try:
        # Initialize browser
        browser = init_browser()

        # Visit Mars Space Images through splinter module
        featuredImageJPL = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(featuredImageJPL)
        time.sleep(1)
        htmlImage = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(htmlImage, 'html.parser')

        # Retrieve background-image url from style tag
        featuredImageURL = soup.find('article')['style']
        featuredImageURL = featuredImageURL.replace('background-image: url(', '').replace(');', '')[1:-1]
        featuredImageURL = 'https://www.jpl.nasa.gov' + featuredImageURL

        # Display full link to featured image
        print(featuredImageURL)

        # Dictionary entry from FEATURED IMAGE
        mars_info['featured_image_url'] = featuredImageURL
        return mars_info
    finally:

        browser.quit()


# MARS WEATHER
def MARSWeather():
    try:
        # Initialize browser
        browser = init_browser()

        # Visit Mars Weather Twitter through splinter module
        weatherURL = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(weatherURL)
        time.sleep(1)
        htmlWeather = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(htmlWeather, 'html.parser')
        latestTweets = soup.find_all('div', class_='js-tweet-text-container')

        # Retrieve all elements that contain news title in the specified range
        for tweet in latestTweets:
            weatherTweet = tweet.find('p').text
            if 'Sol' and 'pressure' in weatherTweet:
                print(weatherTweet)
                break
            else:
                pass

        # Dictionary entry from WEATHER TWEET
        weatherTweet = weatherTweet.replace('InSight ', '')
        weatherTweet = weatherTweet[:weatherTweet.find('hPa') + 3]
        mars_info['weather_tweet'] = weatherTweet
        return mars_info
    finally:

        browser.quit()


# MARS FACTS
def MARSFacts():
    # Visit Mars facts url
    factsURL = 'http://space-facts.com/mars/'
    marsFacts = pd.read_html(factsURL)
    marsDF = marsFacts[0]

    # Assign the columns `['Description', 'Value']`
    marsDF.columns = ['Description', 'Value']
    marsDF.set_index('Description', inplace=True)
    data = marsDF.to_html()

    # Dictionary entry from MARS FACTS
    mars_info['mars_facts'] = data
    return mars_info


# MARS HEMISPHERES
def MARSHemisphere():
    try:
        # Initialize browser
        browser = init_browser()

        hemispheresURL = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemispheresURL)
        time.sleep(1)
        htmlHemispheres = browser.html
        hemisphereImageURLs = []

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(htmlHemispheres, 'html.parser')
        allItems = soup.find_all('div', class_='item')

        hemispheresURL = 'https://astrogeology.usgs.gov'

        # Loop through the items previously stored
        for i in allItems:
            title = i.find('h3').text
            partialImgURL = i.find('a', class_='itemLink product-item')['href']

            # the link that contains the full image website
            browser.visit(hemispheresURL + partialImgURL)
            time.sleep(1)
            partialImgHtml = browser.html
            soup = BeautifulSoup(partialImgHtml, 'html.parser')

            # Retrieve full image source
            imgURL = hemispheresURL + soup.find('img', class_='wide-image')['src']
            hemisphereImageURLs.append({"title": title, "img_url": imgURL})

        mars_info['hemisphereImageURLs'] = hemisphereImageURLs
        return mars_info
    finally:

        browser.quit()