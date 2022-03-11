from django.contrib import admin
from django.urls import path, include
from django.urls import re_path, include
from django.views.generic.base import TemplateView 
from django.contrib.auth import views as auth_views
from django.conf import settings



from music_streaming_app import views as musicapp_views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'),
     name='home'),
    re_path(r'^$', musicapp_views.home, name='home'),
    re_path(r'^register/$', musicapp_views.signup, name='signup'),
    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    re_path('logout/', auth_views.LogoutView.as_view(),{'next_page': settings.LOGIN_REDIRECT_URL}, name='logout'),
    
    
    re_path(r'^account_activation_sent/$', musicapp_views.account_activation_sent, name='account_activation_sent'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        musicapp_views.activate, name='activate'),
    path('music-streaming-app/', include('music_streaming_app.urls')),
]