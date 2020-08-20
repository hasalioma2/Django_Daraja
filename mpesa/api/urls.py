from django.urls import path
from mpesa.api.views import LNMOCallbackApiView

urlpatterns =[
    path('lnm/', LNMOCallbackApiView.as_view(), name= 'lnm-callbackurl')
]