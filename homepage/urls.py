from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path("",views.home,name="home"),
    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    path("register_user",views.register_user,name="register_user"),
    path("user_login",views.user_login,name="user_login"),
    path("send_file",views.send_file,name="send_file")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)