from django.urls import path
from .views import App_thingieList, App_thingieDetail

urlpatterns = [ 
    path('', App_thingieList.as_view(), name='app_list'),
    path('<int:pk>/', App_thingieDetail.as_view(), name='app_detail')
]