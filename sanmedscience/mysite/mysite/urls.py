"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views
from django.conf.urls import url
from django.contrib import admin

from pages.views import HomeView, get_data, ChartData, get_name, ChartData1, HomeView2,HomeView3,HomeView4,HomeView5,HomeView6, ChartData2,ChartData3, ChartData4, ChartData5
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view.as_view()),
    path('narad/', views.narad_view.as_view()),
    url(r'^text_f/x/$', HomeView.as_view(), name='home'),
    url(r'^text_f/t/$', HomeView2.as_view(), name='home'),
    url(r'^text_f/a/$', HomeView3.as_view(), name='home'),
    url(r'^text_f/b/$', HomeView4.as_view(), name='home'),
    url(r'^text_f/c/$', HomeView5.as_view(), name='home'),
    url(r'^text_f/d/$', HomeView6.as_view(), name='home'),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^api/chart/datat/$', ChartData1.as_view()),
    url(r'^api/chart/dataa/$', ChartData2.as_view()),
    url(r'^api/chart/datab/$', ChartData3.as_view()),
    url(r'^api/chart/datac/$', ChartData4.as_view()),
    url(r'^api/chart/datad/$', ChartData5.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^text_f/$', get_name, name='text_f'),

]