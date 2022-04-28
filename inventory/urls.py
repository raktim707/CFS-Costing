from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-entry', views.add_entry, name='add_entry'),
    path('import-from-excel', views.import_from_excel, name='import_excel')
]
