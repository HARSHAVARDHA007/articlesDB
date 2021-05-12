#pip3 install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import re

#path for the chromedriver in the local machine
#download the driver from the https://chromedriver.chromium.org/downloads

PATH='/home/harsha/WebDrivers/chromedriver_linux64/chromedriver'
driver=webdriver.Chrome(PATH)
headerList = ['Article_Link', 'Article_Title', 'Date', 'Author','Description','Topic']
with open('articles.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headerList)
    writer.writeheader()
writeFile = open('articles.csv', 'a')
writer = csv.writer(writeFile)

#functions for each website
#www.thehackernews.com scrapping function

def scrape_hackerNews(link):
    driver.get(link)
    articleList = driver.find_elements_by_css_selector('div.body-post.clear')

    parentList = []
    for element in articleList:
        childList = []
        childList.append(element.find_element_by_css_selector('a.story-link').get_attribute('href') + ' ')
        childList.append(element.find_element_by_css_selector('h2.home-title').text)
        temp = re.sub(r'[^a-zA-Z0-9,\s]', '$', element.find_element_by_css_selector('div.item-label').text)[1:].split('$')
        childList.append(temp[0])
        childList.append(temp[1])
        childList.append(element.find_element_by_css_selector('div.home-desc').text)
        childList.append('Cyber Security')
        parentList.append(childList)
    writer.writerows(parentList)
    writeFile.flush()
    linkToNextPage = driver.find_element_by_css_selector('a.blog-pager-older-link-mobile').get_attribute('href')
    return linkToNextPage

#analyticsvidhya scrapping function

def scrape_analyticsVidhya(link,flag):
    parentList = []
    driver.get(link)
    articles=driver.find_elements_by_css_selector('div.up-up-child.col-sm-6')
    for article in articles:
        childList=[]
        dummy=article.find_element_by_class_name('entry-title')
        childList.append(dummy.find_element_by_css_selector('a').get_attribute('href') + ' ')
        childList.append(article.find_element_by_class_name('entry-title').text)
        childList.append(article.find_element_by_class_name('entry-date').text)
        childList.append(article.find_element_by_class_name('entry-author').text)
        childList.append(article.find_element_by_class_name('i-summary').text)
        if flag==0:
            childList.append('Machine learning')
        if flag==1:
            childList.append('Deep learning')
        if flag==2:
            childList.append('Carrer-in-DataScience')
        parentList.append(childList)
    writer.writerows(parentList)
    writeFile.flush()
    next_page=driver.find_element_by_css_selector('a.next').get_attribute('href')
    return next_page

#www.smashingmagazine.com scrapping function

def scrape_web_development(link,flag):
    driver.get(link)
    articles=driver.find_elements_by_class_name('article--post')
    parentList = []
    for article in articles:
        childList=[]
        dummy=article.find_element_by_class_name('article--post__title')
        childList.append(dummy.find_element_by_css_selector('a').get_attribute('href')+' ')
        childList.append(article.find_element_by_class_name('article--post__title').text)
        article_summary=article.find_element_by_class_name('article--post__teaser').text
        x=article_summary.split('—')
        childList.append(x[0])
        childList.append(article.find_element_by_class_name('red').text)
        x=x[1].split('\n')
        childList.append(x[0])
        if flag==0:
            childList.append('CSS')
        if flag==1:
            childList.append('JAVASCRIPT')
        if flag==2:
            childList.append('REACT')
        if flag==3:
            childList.append('UX DESIGN')
        if flag==4:
            childList.append('VUE')
        if flag==5:
            childList.append('Design Patterns')
        parentList.append(childList)
    writer.writerows(parentList)
    writeFile.flush()
    next_page=driver.find_element_by_class_name('pagination__next')
    next_page_link=next_page.find_element_by_css_selector('a').get_attribute('href')
    return next_page_link

# no of pages from the website for each topic 

link='https://www.analyticsvidhya.com/blog/category/machine-learning/'   
for i in range(15):
    link=scrape_analyticsVidhya(link,0)
link='https://www.analyticsvidhya.com/blog/category/deep-learning/'  
for i in range(10):
    link=scrape_analyticsVidhya(link,1)
link='https://www.analyticsvidhya.com/blog/category/career/'
for i in range(7):
    link=scrape_analyticsVidhya(link,2)
link='https://www.smashingmagazine.com/category/css/'
for i in range(7):
    link=scrape_web_development(link,0)
link='https://www.smashingmagazine.com/category/javascript/'
for i in range(7):
    link=scrape_web_development(link,1)
link='https://www.smashingmagazine.com/category/react/'
for i in range(5):
    link=scrape_web_development(link,2)
link='https://www.smashingmagazine.com/category/ux/'
for i in range(7):
    link=scrape_web_development(link,3)
link='https://www.smashingmagazine.com/category/vue/'
for i in range(2):
    link=scrape_web_development(link,4)
link='https://www.smashingmagazine.com/category/design-patterns'
for i in range(5):
    link=scrape_web_development(link,5)
link='https://thehackernews.com/'
for i in range(10):
    link=scrape_hackerNews(link)

driver.close()
