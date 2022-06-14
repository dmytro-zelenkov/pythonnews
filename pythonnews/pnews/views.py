import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from pnews.models import Headline
import re

def home(request):
    return render(request, 'home.html')

def scrape(request):
  # Defining data for scraping
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url_base = "https://python-forum.io/forum-31-page-"
  #url = "https://python-forum.io/forum-31.html"
  
  page = 1
  # Going 5 pages deep
  while page != 6:
    url = f"{url_base}{page}.html"
    content = session.get(url, verify=False).content
    # Using BeautifulSoup for scraping
    soup = BSoup(content, "html.parser")
    Info = soup.find_all(class_ = 'inline_row')
    
    for post in Info:
      main = post.find_all('a')[1]
      link = url[:url.rfind('/')+1] + main['href']
      title = main.text
      date = post.find(class_='d-none d-sm-none d-md-inline-block').text[2:]
      # Making sure we get only numbers in string and converting to int
      replies = int(''.join(re.findall(r'\d+', post.find(class_='text-dark-75 d-block').text))) 
      views = int(''.join(re.findall(r'\d+', post.find_all('td')[2].text)))
  
      # Writing data to the database
      new_headline = Headline()
      new_headline.title = title
      new_headline.url = link
      new_headline.date = date
      new_headline.replies = replies
      new_headline.views = views
      new_headline.save()
    
    page += 1
#  Redirecting to the main page 
  return redirect("../")

def news_list(request):
    headlines = Headline.objects.all().order_by('-views')[:10]
    context = {
        'object_list': headlines,
    }
    return render(request, "home.html", context)
