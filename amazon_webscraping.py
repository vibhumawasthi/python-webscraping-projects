#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


# In[2]:


# function to extract title
def get_title(soup):
    
    try:
        title_string = new_soup.find("span", attrs={"id": "productTitle"}).text.strip()
    
    except AttributeError:
        title_string = ''
    
    return title_string

#function to extract price
def get_price(soup):
    
    try:
        price = new_soup.find("span", attrs={"class": "a-price-whole"}).text
    
    except AttributeError:
        price = ''
    
    return price

#function to extract rating
def get_rating(soup):
    
    try:
        rating = new_soup.find("span", attrs={"class": "a-icon-alt"}).text
    
    except AttributeError:
        rating = ''
    
    return rating

#function to extract total ratings given
def get_rated(soup):
    
    try:
        rated = new_soup.find("span", attrs={"id": "acrCustomerReviewText"}).text
    
    except AttributeError:
        rated = ''
    
    return rated


# In[3]:


if __name__ == '__main__':
    # headers for request
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    
    # webpage url
    URL = "https://www.amazon.in/s?k=one+piece+tshirt&ref=nb_sb_noss"
    
    # HTTP request
    webpage = requests.get(URL, headers=HEADERS)
    
    # soup object containing all data
    soup = BeautifulSoup(webpage.content, 'html.parser')
    
    # fetch links as list of tag object
    links = soup.find_all("a", attrs = {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    
    # store the links
    links_list = []
    
    # loop for extracting links from Tag objects
    for link in links:
        links_list.append(link.get('href'))
    
    
   # for link in links:
    #    link_y = link.get('href')
    #    link_z = link_y.split("%2F", 1)[1].replace("%2F", "/")
    #    links_list.append(link_z)
    
    d = {"title":[], "price": [], "rating":[], "total_rated": []}
    
    # loop for extracting product details from each link
    for link in links_list:
        new_webpage = requests.get('https://amazon.in' + link, headers = HEADERS)
        
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")
    
    
    # function calls to display all necessary product information
    d['title'].append(get_title(new_soup))
    d['price'].append(get_price(new_soup))
    d['rating'].append(get_rating(new_soup))
    d['total_rated'].append(get_rated(new_soup))
    
    
    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df['title'].replace('', np.nan, inplace = True)
    amazon_df = amazon_df.dropna(subset = 'title')
    amazon_df.to_csv("amazon_raw_data.csv", header = True, index = False)
    
    
    
    


# In[ ]:


amazon_df


# In[ ]:




