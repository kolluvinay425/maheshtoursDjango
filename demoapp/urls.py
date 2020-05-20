from . import views
from django.urls import path
app_name = 'demoapp'


urlpatterns = [

    path('',views.home,name="home"),
    path('<int:tour_id>/',views.detail,name="detail"),
    path('about/',views.contact,name="contact"),
    path('travels/',views.tour_package,name="tour_package"),
 
   
]