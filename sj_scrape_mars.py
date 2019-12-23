# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import requests

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

def scrape():

    # Retrieve NASA Mars News page
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Use BeautifulSoup to get 'content_title' and 'rollover_description_inner' results 

    slide_elem = soup.select_one('ul.item_list li.slide')
    results = soup.find('div', class_= "content_title").get_text()
    
    # Use BeautifulSoup to get 'rollover_description_inner' results 
    results_para = soup.find('div', class_= "rollover_description_inner").get_text


    # JPL Mars Space Images - Featured Image

    from splinter import Browser
    from splinter.exceptions import ElementDoesNotExist
    from bs4 import BeautifulSoup

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    full_image = browser.find_by_id("full_image")
    full_image.click()

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    featured_image_url = soup.find('img', class_='fancybox-image')


    # Mars Facts 
    import pandas as pd

    url = 'https://space-facts.com/mars/'

    # Use read_html Pandas function to scrape tabular data from website
    tables = pd.read_html(url)

    # Make DataFrame, set column names, and index
    df = tables[0]
    df.columns = ['Topic', 'Fact']
    df.set_index('Topic', inplace=True)

    # Generate HTML table from DataFramer
    html_table = df.to_html()

    # To remove unwanted new lines to clean up the table (see whether this is needed by putting previous table in html file)
    # html_table.replace('\n', '')


    # Store data in a dictionary

    mars_data = {
            "Mars_News_Title": results,
            "Mars_News_Para": results_para,
            "Mars_Facts": html_table,        
            "Mars_Space_Images": featured_image_url
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
