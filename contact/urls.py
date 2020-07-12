from . import views
from django.urls import path
app_name = 'contact'


urlpatterns = [

    
   path('contact/',views.sendmail,name="sendmail"),
   path('success/',views.success,name="success"),
 
   
]