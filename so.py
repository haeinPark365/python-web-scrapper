import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python"

def get_last_page():
  request = requests.get(URL)
  soup = BeautifulSoup(request.text,"html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
  last_pages = pages[-2].find("span").string
  return int(last_pages)

def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(page)

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs()
  return jobs