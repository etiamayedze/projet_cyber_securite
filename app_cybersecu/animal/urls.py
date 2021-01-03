from django.urls import path
from . import views

urlpatterns = [
    path('animal/', views.animal, name='addanimal'),
    path('updateanimal/<int:id>/', views.updateanimal, name='updateanimal'),
    path('deleteanimal/<int:id>/', views.deleteanimal, name='deleteanimal'),
    path('listanimal/', views.listanimaux, name='listanimal'),
    path('parent/', views.parent, name='addparent'),
    path('updateparent/<int:id>/', views.updateparent, name='updateparent'),
    path('deleteparent/<int:id>/', views.deleteparent, name='deleteparent'),
    path('listparent/', views.listparent, name='listparent'),
    path('typeanimal/', views.typeanimal, name='addtypeanimal'),
    path('updatetypeanimal/<int:id>/', views.updatetypeanimal, name='updatetypeanimal'),
    path('deletetypeanimal/<int:id>/', views.deletetypeanimal, name='deletetypeanimal'),
    path('listtypeanimal/', views.listtypeanimal, name='listtypeanimal'),
    path('medecin/', views.medecin, name='addmedecin'),
    path('updatemedecin/<int:id>/', views.updatemedecin, name='updatemedecin'),
    path('deletemedecin/<int:id>/', views.deletemedecin, name='deletemedecin'),
    path('listmedecin/', views.listmedecin, name='listmedecin'),
    path('rendezvous/', views.rendezvous, name='addrendezvous'),
    path('updaterendezvous/<int:id>/', views.updaterendezvous, name='updaterendezvous'),
    path('deleterendezvous/<int:id>/', views.deleterendezvous, name='deleterendezvous'),
    path('listrendezvous/', views.listrendezvous, name='listrendezvous'),
]
