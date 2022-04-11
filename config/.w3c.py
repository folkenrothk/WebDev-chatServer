import sys
import json
import requests
import os

def parse_response(response: str) -> list:
  return json.loads(response)

def evaluate(response: dict) -> bool:
  if len(response["messages"]) > 0:
    return False
  return True

def validate_html(endpoint: str, page: str) -> bool:
  validator = requests.get(
    "https://validator.w3.org/nu/",
    params = {
      "doc":f"{endpoint}{page}",
      "out":"json"
    }
  )

  response = parse_response(validator.text)

  return evaluate(response)

def validate_css(endpoint: str, page: str) -> bool:
  validator = requests.get(
    "https://jigsaw.w3.org/css-validator/validator",
    params = {
      "uri":f"{endpoint}{page}",
      "profile":"css3",
      "output":"json"
    }
  )

  response = json.loads(validator.text)

  return response["cssvalidation"]["validity"] == "true"


def main():

  pages_api = os.getenv("PAGES_URL")
  data = json.loads(pages_api)
  endpoint = data["html_url"]
  page = sys.argv[1]

  valid = True

  if page.endswith(".css"):
    response = validate_css(endpoint, page)
  else:
    response = validate_html(endpoint, page)

  if valid:
    sys.exit(0)
  sys.exit(1)

if __name__ == "__main__":
  main()
