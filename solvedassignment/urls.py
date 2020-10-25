"""solvedassignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from assignment import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('register/', views.register, name = "register"),
    #path('login/', views.signin, name = "login",),
    path('logout/', views.signout, name = "logout"),
    path('payment/', views.payment, name = "payment"),
    path('', views.index, name = "home"),
    path('nmims', views.nmims, name = "nmims"),
    path('amity', views.amity, name = "amity"),
    path('request', views.requested_assignment, name = 'requested'),
    path('profile', views.myprofile, name = 'myprofile'),
    path('assignment/<str:sub_code>', views.assignment_sol, name= "solution")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
