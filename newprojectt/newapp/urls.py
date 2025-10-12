from django.urls import path
from newapp.views import *

urlpatterns = [
    path("",home,name="home"),
    path("register/",register,name="register"),
    path("sign/",sign,name="sign"),
    path("logout_func",logout_func,name="logout_func"),
    path("delete/<id>/",delete_task,name="delete_task"),
    path("update/<id>/",update_task,name="update_task"),

]