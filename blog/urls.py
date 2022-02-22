from django.urls import path
from .views import * 


urlpatterns = [
    path('', list_page_view, name='blog-list'),

]






