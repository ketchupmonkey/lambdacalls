#!/usr/bin/python

import requests
import simplejson

api_url = "http://api.openweathermap.org"
def weathercall():

  url = "{}{}" . format(api_url, '/data/2.5/weather?id=2193733&APPID=5af0611c68527acab60a69445dbb28e1&units=metric')
  result=requests.get(url)
  # print result
  print url
  # return url;
  return result.json()


print weathercall()
