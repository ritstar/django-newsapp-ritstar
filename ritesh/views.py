from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests;
import json;
from . import forms
from newsapi import NewsApiClient
from django.core.mail import send_mail
# Create your views here.
try:
    newsapi = NewsApiClient(api_key='23f1ea61ddf444d7b98b68f746262f26')
    top_headlines = newsapi.get_top_headlines(category='technology',language='en',country='in')
    all_articles = newsapi.get_everything(sources='bbc-news,the-verge,crypto coins news',language='en',sort_by='relevancy',page=2,)
except Exception:
    print("Troubling Problem..............")
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

def mail_me(request):
    
    body = list()
    for i in top_headlines['articles']:
        body.append(i['title'])
    j=1
    body_s = str()
    for i in body:
        body_s = body_s + str(j) + ". " + i + '\n'
        j=j+1   
    form_mail= forms.mailme()
    if request.method == 'POST':
        #email = EmailMessage("Headlines",'body[0]',request.POST['email'])
        try:
            send_mail('Headlines', body_s, 'ritesh02700@gmail.com', [request.POST['email']])
            return HttpResponse("Email Sent")
        except Exception:
            return HttpResponse("Email Not Sent : Fatal Error")


    return render(request,'mail_me.html',context={'form_mail': form_mail})