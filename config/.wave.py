import sys
import json
import requests
import os

def main():

  pages_api = os.getenv("PAGES_URL")
  wave_api = os.getenv("WAVE_API")

  data = json.loads(pages_api)
  endpoint = data["html_url"]
  page = sys.argv[1]

  validator = requests.get(
    "https://wave.webaim.org/api/request",
    params = {
      "key":wave_api,
      "url":f"{endpoint}{page}"
    }
  )

  response = json.loads(validator.text)

  contrast_count = int(response['categories']['contrast']['count'])
  error_count = int(response['categories']['error']['count])

  if contrast_count + error_count < 1:
    sys.exit(0)
  sys.exit(1)

if __name__ == "__main__":
  main()
