from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
import urllib.request
import socket, time
import urllib.parse
import requests
import urllib
from urllib.request import urlopen

from rest_framework.views import APIView
from rest_framework.response import Response


from pages.models import NameForm


class home_view(TemplateView):
    template_name = "index.html"


class narad_view(TemplateView):
    template_name = "narad.html"


class base_view(TemplateView):
    template_name = "base.html"

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'text_f.html', {'form': form})

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"ResponseTime": 0.94})

class HomeView2(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts1.html', {"ResponseTime": 0.94})

class HomeView3(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart2.html', {"ResponseTime": 0.94})


class HomeView4(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart3.html', {"ResponseTime": 0.94})

class HomeView5(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart4.html', {"ResponseTime": 0.94})

class HomeView6(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart5.html', {"ResponseTime": 0.94})




def get_data(request, *args, **kwargs):
    data = {
        "responseTime": 0.1,
        "LoadTime": 0.4,
    }
    return JsonResponse(data) # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        url = 'http://www.viriminfotech.com/'

        try:
            r = requests.get(url, timeout=6)
            r.raise_for_status()
            respTime = str(round(r.elapsed.total_seconds(), 2))



        except requests.exceptions.HTTPError as err01:
            print("HTTP error: ", err01)
        except requests.exceptions.ConnectionError as err02:
            print("Error connecting: ", err02)
        except requests.exceptions.Timeout as err03:
            print("Timeout error:", err03)
        except requests.exceptions.RequestException as err04:
            print("Error: ", err04)
        labels = ["responseTime"]

        default_items = [respTime]

        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

class ChartData1(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):


        url = 'http://www.google.com/'

        try:
            r = requests.get(url, timeout=6)
            r.raise_for_status()
            respTime = str(round(r.elapsed.total_seconds(), 2))



        except requests.exceptions.HTTPError as err01:
            print("HTTP error: ", err01)
        except requests.exceptions.ConnectionError as err02:
            print("Error connecting: ", err02)
        except requests.exceptions.Timeout as err03:
            print("Timeout error:", err03)
        except requests.exceptions.RequestException as err04:
            print("Error: ", err04)


        start = time.time()
        _data = urllib.request.urlopen(url).read()
        load_tm = time.time() - start


        t1 = time.time()
        r = requests.get(url)
        t2 = time.time()
        tim = str(t2 - t1)



        labels = ["responseTime","LoadTime","RoundTripTime"]

        default_items = [respTime,load_tm,tim]

        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

class ChartData2(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):


        url = 'http://www.gmail.com'

        try:
            r = requests.get(url, timeout=6)
            r.raise_for_status()
            respTime = str(round(r.elapsed.total_seconds(), 2))



        except requests.exceptions.HTTPError as err01:
            print("HTTP error: ", err01)
        except requests.exceptions.ConnectionError as err02:
            print("Error connecting: ", err02)
        except requests.exceptions.Timeout as err03:
            print("Timeout error:", err03)
        except requests.exceptions.RequestException as err04:
            print("Error: ", err04)


        start = time.time()
        _data = urllib.request.urlopen(url).read()
        load_tm = time.time() - start


        t1 = time.time()
        r = requests.get(url)
        t2 = time.time()
        tim = str(t2 - t1)



        labels = ["responseTime","LoadTime","RoundTripTime"]

        default_items = [respTime,load_tm,tim]

        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


class ChartData3(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):


        url = 'http://www.amazon.in'

        try:
            r = requests.get(url, timeout=6)
            r.raise_for_status()
            respTime = str(round(r.elapsed.total_seconds(), 2))



        except requests.exceptions.HTTPError as err01:
            print("HTTP error: ", err01)
        except requests.exceptions.ConnectionError as err02:
            print("Error connecting: ", err02)
        except requests.exceptions.Timeout as err03:
            print("Timeout error:", err03)
        except requests.exceptions.RequestException as err04:
            print("Error: ", err04)


        start = time.time()
        _data = urllib.request.urlopen(url).read()
        load_tm = time.time() - start


        t1 = time.time()
        r = requests.get(url)
        t2 = time.time()
        tim = str(t2 - t1)



        labels = ["responseTime","LoadTime","RoundTripTime"]

        default_items = [respTime,load_tm,tim]

        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

class ChartData4(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):


        url = 'http://www.viriminfotech.com/'

        try:
            r = requests.get(url, timeout=6)
            r.raise_for_status()
            respTime = str(round(r.elapsed.total_seconds(), 2))



        except requests.exceptions.HTTPError as err01:
            print("HTTP error: ", err01)
        except requests.exceptions.ConnectionError as err02:
            print("Error connecting: ", err02)
        except requests.exceptions.Timeout as err03:
            print("Timeout error:", err03)
        except requests.exceptions.RequestException as err04:
            print("Error: ", err04)


        start = time.time()
        _data = urllib.request.urlopen(url).read()
        load_tm = time.time() - start


        t1 = time.time()
        r = requests.get(url)
        t2 = time.time()
        tim = str(t2 - t1)



        labels = ["responseTime","LoadTime","RoundTripTime"]

        default_items = [respTime,load_tm,tim]

        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

class ChartData5(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):


        url = 'http://www.svvv.edu.in'

        try:
            r = requests.get(url, timeout=6)
            r.raise_for_status()
            respTime = str(round(r.elapsed.total_seconds(), 2))



        except requests.exceptions.HTTPError as err01:
            print("HTTP error: ", err01)
        except requests.exceptions.ConnectionError as err02:
            print("Error connecting: ", err02)
        except requests.exceptions.Timeout as err03:
            print("Timeout error:", err03)
        except requests.exceptions.RequestException as err04:
            print("Error: ", err04)


        start = time.time()
        _data = urllib.request.urlopen(url).read()
        load_tm = time.time() - start


        t1 = time.time()
        r = requests.get(url)
        t2 = time.time()
        tim = str(t2 - t1)



        labels = ["responseTime","LoadTime","RoundTripTime"]

        default_items = [respTime,load_tm,tim]

        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

