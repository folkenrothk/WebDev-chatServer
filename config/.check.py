import requests
import sys
import os

from os.path import exists
from bs4 import BeautifulSoup

def parse_html(path: str) -> BeautifulSoup:
  with open(path, "r") as fh:
    content = fh.read()
  return BeautifulSoup(content, "html.parser")

def check_valid_urls(html: BeautifulSoup) -> bool:
  links = html.find_all("a")
  links = [link for link in links if not link["href"].startswith("#")]
  for link in links:
    response = requests.get(link["href"])
    status = response.status_code
    if status < 200 and status > 403:
      return False
  return True

def check_local_files(html: BeautifulSoup) -> bool:
  images = html.find_all("img")
  for image in images:
    if not exists(f"docs/{image['src']}"):
      print(image['src'], False)
      return False
  return True

def check_tag(html: BeautifulSoup, tag: str, count: int = 1) -> bool:
  tags = html.find_all(tag)
  if len(tags) < count:
    return False
  return True

def main():
  file = str(sys.argv[1])
  tags = sys.argv[2:-1]
  try: count = int(sys.argv[-1])
  except: count = 1
  html = parse_html(file)

  valid_tags = True
  valid_uri = True

  if "check_uri" in tags:
    tags.remove("check_uri")
    valid_uri = check_valid_urls(html) and check_local_files(html)

  for tag in tags:
    valid_tags = check_tag(html, tag, count)

  if valid_uri and valid_tags:
    sys.exit(0)
  sys.exit(1)

if __name__ == "__main__":
  main()
