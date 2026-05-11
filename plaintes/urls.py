from django.urls import path

from . import views


urlpatterns = [
    path('', views.identification, name='identification'),
    path('identification/', views.identification, name='identification_page'),
    path('changer-utilisateur/', views.changer_utilisateur, name='changer_utilisateur'),
    path('plaintes/', views.plainte_list, name='plainte_list'),
    path('plaintes/export-excel/', views.plainte_export_excel, name='plainte_export_excel'),
    path('plaintes/ajouter/', views.plainte_create, name='plainte_create'),
    path('plaintes/<int:pk>/', views.plainte_detail, name='plainte_detail'),
    path('plaintes/<int:pk>/modifier/', views.plainte_update, name='plainte_update'),
    path('plaintes/<int:pk>/supprimer/', views.plainte_delete, name='plainte_delete'),
]
