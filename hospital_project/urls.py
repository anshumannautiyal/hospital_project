from django.conf.urls import include, url,patterns
from django.contrib import admin
from hospital_recors import views

# here we have linked the urls with the views.py file functions 
# for example on opening loacalhost:8000/index we call index function which is inside views.py file
urlpatterns = patterns('',
    # url(r'^admin'),
    url(r'^index',views.index,name='index'),
	url(r'^open',views.open,name='open'),
    url(r'^make_new_voyage',views.make_new_voyage,name='make_new_voyage'),
	)
   

