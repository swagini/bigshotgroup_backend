
from django.contrib import admin
from django.urls import path
from bigshotApp.users import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getuserdetails/',GetUserDetails.as_view()),
   path('insertuserdetails/',InsertUserDetails.as_view()),
   path('getotpgeneration/',GetOtpGeneration.as_view()),
   path('updatepassword/',UpdatePassword.as_view())
]
