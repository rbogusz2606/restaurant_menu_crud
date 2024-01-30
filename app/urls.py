from django.urls import path

from . import views

urlpatterns = [
    path("menu", views.MenuList),
    path("menu/<int:id>", views.Show_Change_Delete_Obj),
    ]