
from django.urls import path, include

from catalog.views import contacts, home

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', home, name='home'),

]