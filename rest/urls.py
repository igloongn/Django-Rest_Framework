from django.urls import path, re_path, include
from . import views as v

# Router
from rest_framework.routers import DefaultRouter
default_router=DefaultRouter()
default_router.register('inside', v.HelloViewsSet, basename="viewset")


urlpatterns = [
    # APIView
    path('apiviews/', v.HelloApiview.as_view()),
    # ViewSets
    path('viewset/', include(default_router.urls))

]