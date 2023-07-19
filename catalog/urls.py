
from django.urls import path, include

import catalog
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import contacts, home

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', catalog.views.home, name='home'),

]