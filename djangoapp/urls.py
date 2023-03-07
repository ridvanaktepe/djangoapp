from django.contrib import admin
from django.urls import path, include
from djangorestapp import views
from django.conf.urls import re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginpage, name='login'),
    path('index/', views.index, name='index'),
    path('signup/', views.signUp, name='signup'),
    path('logout', views.logoutpage, name='logout'),
    path('addnew', views.addUav),
    path('edit/<int:id>', views.editUav),
    path('update/<int:id>', views.updateUav),
    path('delete/<int:id>', views.deleteUav),

    re_path('', include('django_dyn_dt.urls')),
    re_path(r'^', include('djangorestapp.urls'))
]
