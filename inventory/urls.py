from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.home, name='home'),
    path('add-entry', views.add_entry, name='add_entry'),
    path('<int:pk>/general-detail', views.rfq_detail, name='rfq_detail'),
    path('<int:pk>/edit-general-data',
         views.EditRFQView.as_view(), name='edit_rfq'),
    path('<int:pk>/edit-material',
         views.editMaterialView, name='edit_material'),
    path('import-from-excel', views.import_from_excel, name='import_excel'),
    path('primary-process', views.primaryProcess, name='primary_process'),
    path('secondary-process', views.secondaryProcess, name='secondary_process'),
    path('add-primary', views.addPrimaryProcess, name='add_primary'),
    path('manage-users', views.manageUser, name='manage_user'),
    path('add-user', views.addNewUser, name='add_user'),
    path('configure-material', views.adminMaterialConfigure,
         name="admin_material_configure"),
    path('choose-material', views.materialDimensions, name='choose_material'),
    path('general-data', views.rfqGeneralData, name='general_data'),
    path('material-costing', views.materialCost, name='material_cost'),
    path('process-cost', views.processCost, name='process_cost'),
    path('search-parts', views.searchStandardPart, name='search_parts'),
    path('', views.welcome, name='welcome')
]
