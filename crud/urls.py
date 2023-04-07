from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createcontact/', views.createcontact, name="create_contact"),
    path('updatecontact/<str:pk>', views.updatecontact, name="update_contact"),
    path('deletecontact/<str:pk>', views.deletecontact, name="delete_contact"),

]