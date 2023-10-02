from django.shortcuts import render, HttpResponse
from bs4 import BeautifulSoup
import requests
# Create your views here.


def test(request):
    r = requests.get('https://pypi.org/project/beautifulsoup4/s')
    soup = BeautifulSoup(r.text, 'lxml')
    print(soup.title.string)
    return HttpResponse("hello")
