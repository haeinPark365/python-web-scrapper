import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/취업?q=python&limit={LIMIT}"

def get_last_pages() : 
  request = requests.get(URL)
  soup = BeautifulSoup(request.text, ("html.parser"))

  pagination = soup.find("div", {"class": "pagination"})
  links = pagination.find_all("span", {"class" : "pn"})
  pages = []

  for link in links[:-1]:
    pages.append(int(link.string))

  max_page = pages[-1]
  
  return max_page


def extract_job(job_soup):
  title = job_soup.find("h2",{"class" : "title"}).find("a")["title"]
  company = job_soup.find("span", {"class" : "company"})
  location = job_soup.find("div", {"class" : "recJobLoc"})["data-rc-loc"]

  company_anchor = company.find("a")
  if company_anchor is None:
    company = company.string
  else:
    company = company_anchor.string
  company = company.strip()

  job_id = job_soup["data-jk"]

  return {'title':title, 'company':company, 'location':location, 'link': f"https://kr.indeed.com/viewjob?jk={job_id}"}


def extract_jobs(last_page):
  jobs = []
  
  for page in range(last_page): 
    print(f"page number : {page}")
    request = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(request.text,"html.parser")
    results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})

    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs():
  last_page = get_last_pages()
  jobs = extract_jobs(last_page)
  return jobs


"""
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("div", {"class" : "pagination"})

  links = pagination.find_all('a')
  pages =[]

  for link in links[:-1]:
    pages.append(int(link.string))

  max_page = pages[-1]
  return max_page


def extract_indeed_jobs(last_page):
  jobs = []
  #for page in range(last_page):
  result = requests.get(f"{URL}&start{0*LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
  for result in results:
    title = result.find("h2", {"class":"title"}).find("a")["title"]
    print(title)
  return jobs
"""