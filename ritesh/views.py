from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests;
import json;
from . import forms
from newsapi import NewsApiClient
from django.core.mail import EmailMessage
# Create your views here.
newsapi = NewsApiClient(api_key='23f1ea61ddf444d7b98b68f746262f26')
top_headlines = newsapi.get_top_headlines(category='technology',language='en',country='in')
all_articles = newsapi.get_everything(sources='bbc-news,the-verge,crypto coins news',language='en',sort_by='relevancy',page=2,)

def index(request):
    try:
        url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=23f1ea61ddf444d7b98b68f746262f26';
        google_url = 'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=23f1ea61ddf444d7b98b68f746262f26'
    

        ind_dic = { 'articles': all_articles, 'headl' : top_headlines}

        return render(request,'index.html',context=ind_dic)
    except Exception:
        print("Troubling Problem..............")
def rit(request):
    return HttpResponse("This is Rit")

def public_news(request):
    ind_dic = { 'articles': all_articles, 'headl' : top_headlines}
    return render(request,'public_news.html',context=ind_dic)

def form_view(request):
    form = forms.FormName()

    return render(request,'form/form_view.html',{'forms' : form})