from splinter import Browser
from bs4 import BeautifulSoup
import time
import requests
import pprint
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

data={}
data



def scrape_info():
    # Browser = init_browser()

    url = 'https://mars.nasa.gov/news/'
    response  = requests.get(url)
    response

    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div',class_='slide')

    headlines=[]
    headlines

    for result in results:
        # Error handling
        try:
            # Identify and return title of listing
            title = result.find(class_="content_title").a.text
            # Identify and return price of listing
            paragraph = result.find(class_="rollover_description_inner").text
            if (title and paragraph):
                # And the anchor has non-blank text...
                # Append the td to the list
                headlines.append({'title':title,'paragraph':paragraph})
                    

            # Print results only if title, price, and link are available
            if (title and paragraph):
                print('-------------')
                # print(title)
                # print(paragraph)
        except AttributeError as e:
            print(e)

    # Close the browser after scraping
    # browser.quit()
    data['title'] = headlines[0]['title']
    data['paragraph'] = headlines[0]['paragraph']
    # data['featured_image_url'] = featured()
    # data['mars_weather'] = mars_tweet()
    # data['mars_html'] = mars_html()
    # data['hemisphere_image_urls'] = mars_hemi()
    print(data)

    return data



def image():
    browser = init_browser()
    # executable_path = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **executable_path, headless=True)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    slides = soup.find('div', class_="carousel_items")
    a = slides.find('a')
    href = a['data-fancybox-href']
    featured_image_url = 'https://www.jpl.nasa.gov' + href


    print("Featured Image", featured_image_url)

    return featured_image_url


def mars_tweet():
    # browser = init_browser()
    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(twitter_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    result = soup.find('div', class_="js-tweet-text-container")
    tweet = result.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    print(tweet)

    return tweet

def mars_html():
    # browser = init_browser()
    mars_html = pd.read_html("https://space-facts.com/mars/")[0]
    mars_html

    mars_html.columns = ['Description', 'Value']
    mars_html['Description'] = mars_html['Description'].str.replace(':', '')
    mars_html.set_index('Description', inplace = True)
    mars_html = mars_html.to_html()
    mars_html

    print("Print of html from SCRAPE PY:", mars_html)

    return mars_html

def mars_hemi():
    # browser = init_browser()
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)

    url_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hemi)

    # HTML object
    html_hemi = browser.html

    # Parse HTML with Beautiful Soup
    soup_hemi = BeautifulSoup(html_hemi, 'html.parser')

    # Retrieve all elements that contain book information
    items = soup_hemi.find_all('div', class_='item')

    hemisphere_image_urls = []

    # Iterate through each book
    for item in items:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        # link = item.find('a')
        # href = link['href']
        titles = item.find('h3').text
        print(titles)
    #     urls = 'https://astrogeology.usgs.gov' + href
    #     print(urls)
        browser.click_link_by_partial_text(titles)
    #     time.sleep(1)
        html_subpage = browser.html
        soup_subpage = BeautifulSoup(html_subpage, 'html.parser')
        img_url = soup_subpage.find('div', 'downloads').ul.li.a['href']
        browser.back()
        hemisphere_image_urls.append({"title": titles, "img_url": img_url})

    print(hemisphere_image_urls)

    return hemisphere_image_urls

