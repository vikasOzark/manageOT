from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name = 'home'),

    path('add_Ot/', views.add_Ot, name = 'add_Ot'),
    path('add_ex/<int:pk>', views.add_Ot, name = 'add_ex'),

    path('adminsite/', views.adminPage, name = 'adminSite'),
    path('signUp/', views.signUp, name = 'signUp'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logOut, name = 'logout'),
    path('add_employee/', views.add_employee, name = 'add_employee')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)