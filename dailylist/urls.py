from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.list, name="list"),
    path("add_item/", views.add_item, name="add_item"),
    path("delete_item/<int:item_id>", views.delete_item, name="delete_item"),
    path("update_item/<int:item_id>", views.update_item, name="update_item"),
    path("purchased/<int:item_id>", views.purchased, name="purchased"),

]





