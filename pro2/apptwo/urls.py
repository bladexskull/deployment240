from django.urls import path,include
from apptwo import views


app_name='apptwo'
urlpatterns=[
 path('',views.new,name='new'),
 path('help2/',views.formcall,name='formcall'),
 path('check/' ,views.index, name='index'),
 path('help/',views.help,name='help')

]
