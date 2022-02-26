from django.urls import path, re_path
from . import views as v


urlpatterns = [
    path('first/', v.HelloApiview.as_view(), name='first')
]