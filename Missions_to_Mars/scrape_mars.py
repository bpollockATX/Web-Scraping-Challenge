#!/usr/bin/env python
# coding: utf-8

# In[1]:

def scrape():
    from splinter import Browser
    import requests
    from bs4 import BeautifulSoup
    import time
    import pandas as pd


    # In[2]:


    # get_ipython().system('which chromedriver')
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)


    # In[3]:


    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(2)
    response = requests.get(url)


    # In[4]:


    # Set HTML, let sleep for 30 seconds for whole page to load
    html = browser.html
    # time.sleep(30)

    soup = BeautifulSoup(html, 'html.parser')


    # In[5]:


    # Find Latest Title, Paragraph from mars.nasa.gov/news/
    list_container = soup.find_all('div', class_ = 'image_and_description_container')[0]
    # list_container
    new_title_results = list_container.find('div', class_ = 'content_title').text

    new_paragraph_results = list_container.find('div', class_ = 'article_teaser_body').text


    # In[6]:


    # Use splinter to inspect JPL site
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    time.sleep(2)


    # In[7]:


    jpl_html = browser.html
    soup = BeautifulSoup(jpl_html, 'html.parser')


    # In[8]:


    fancybox = soup.find('a', class_ = 'button fancybox')
    img_link = fancybox['data-link']


    # In[9]:


    # Visit img link and set new Browser HTML
    browser.visit(f'https://www.jpl.nasa.gov{img_link}')
    new_jpl_url = browser.html


    # In[10]:


    soup_2 = BeautifulSoup(new_jpl_url, 'html.parser')


    # In[11]:


    # Grab image tag from main image component
    featured_image_url = soup_2.find('img', class_ = "main_image")['src']
    # print(main_image)

    featured_image_url = (f'https://www.jpl.nasa.gov{featured_image_url}')


    # In[12]:


    # Visit Mars Weather Twitter
    browser.visit('https://twitter.com/marswxreport?lang=en')
    time.sleep(2)
    twitter_html = browser.html


    # In[13]:


    soup_3 = BeautifulSoup(twitter_html, 'html.parser')


    # In[14]:


    # top_post = soup_3.find_all(attrs={"dir": "auto"})
    mars_weather = soup_3.find('div', class_ = 'css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').text


    # In[15]:


    # Mars facts section
    mars_html = pd.read_html('http://space-facts.com/mars/')


    # In[16]:


    mars_df = pd.DataFrame({"Attribute": mars_html[0].iloc[:,0]
                            ,"Measurement": mars_html[0].iloc[:,1]})
    # mars_df
    mars_df_html = mars_df.to_html()


    # In[17]:


    # Visit the USGS Astrogeology site
    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    time.sleep(2)
    usgs_html = browser.html


    # In[18]:


    soup_4 = BeautifulSoup(usgs_html, 'html.parser')


    # In[19]:


    # Set paths for each of the larger images
    cerberus_slug = soup_4.find_all('div', class_ = 'item')[0].find('a', class_ = 'itemLink product-item')['href']
    schiaparelli_slug = soup_4.find_all('div', class_ = 'item')[1].find('a', class_ = 'itemLink product-item')['href']
    syrtis_slug = soup_4.find_all('div', class_ = 'item')[2].find('a', class_ = 'itemLink product-item')['href']
    valles_slug = soup_4.find_all('div', class_ = 'item')[3].find('a', class_ = 'itemLink product-item')['href']
    # 
    # cerberus_slug
    # schiaparelli_slug
    # syrtis_slug
    # valles_slug


    # In[20]:


    # Build the URLs
    cerberus_url = f'https://astrogeology.usgs.gov{cerberus_slug}'
    schiaparelli_url = f'https://astrogeology.usgs.gov{schiaparelli_slug}'
    syrtis_url = f'https://astrogeology.usgs.gov{syrtis_slug}'
    valles_url = f'https://astrogeology.usgs.gov{valles_slug}'

    # valles_url


    # In[21]:


    # Get Cerberus Image
    browser.visit(cerberus_url)
    time.sleep(2)
    cerberus_html = browser.html

    cerberus_soup = BeautifulSoup(cerberus_html, 'html.parser')

    cerberus_img_url = cerberus_soup.find('li').find('a')['href']
    


    # In[22]:


    # Get Schiaparelli Image
    browser.visit(schiaparelli_url)
    time.sleep(2)
    schiaparelli_html = browser.html

    schiaparelli_soup = BeautifulSoup(schiaparelli_html, 'html.parser')

    schiaparelli_img_url = schiaparelli_soup.find('li').find('a')['href']
    


    # In[23]:


    # Get Syrtis Image
    browser.visit(syrtis_url)
    time.sleep(2)
    syrtis_html = browser.html

    syrtis_soup = BeautifulSoup(syrtis_html, 'html.parser')

    syrtis_img_url = syrtis_soup.find('li').find('a')['href']
    


    # In[24]:


    # Get Valles Image
    browser.visit(valles_url)
    time.sleep(2)
    valles_html = browser.html

    valles_soup = BeautifulSoup(valles_html, 'html.parser')

    valles_img_url = valles_soup.find('li').find('a')['href']
    


    # In[25]:


    # Store hemisphere image URLs in Dictionary
    hemisphere_image_urls = [{"title": "Cerberus Hemisphere", "img_url": cerberus_img_url}
                            ,{"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_img_url}
                            ,{"title": "Syrtis Hemisphere", "img_url": syrtis_img_url}
                            ,{"title": "Valles Hemisphere", "img_url": valles_img_url}]
    


#store in dicitonary
    mars_data = {
        "news_title": new_title_results,
        "news_p": new_paragraph_results,
        "img_url": featured_image_url,
        "mars_weather": mars_weather,
        "mars_info": mars_df_html,
        "hemispheres": hemisphere_image_urls
        }
    
    return mars_data
# print(scrape())

# In[ ]:





# In[ ]:

