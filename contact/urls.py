from . import views
from django.urls import path
app_name = 'contact'


urlpatterns = [

    
   path('contact/',views.send_mail,name="send_mail"),
   path('success/',views.success,name="success"),
 
   
]