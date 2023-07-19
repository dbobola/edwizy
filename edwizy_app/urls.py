from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('base', views.base, name='base'),
    path('trades', views.trades, name='trades'),
    path('add_bot', views.addbot, name='addbot'),
    path('analytics', views.analytics, name='analytics'),
    path('settings', views.settings, name='settings'),
    path('data_view', views.data_view, name='data_view'),
    path('update_bot', views.update_bot, name='update_bot'),
    path('pause_bot', views.pause_bot, name='pause_bot'),
    path('activate_bot', views.activate_bot, name='activate_bot'),
    path('delete_bot', views.delete_bot, name='delete_bot'),
    path('calcprofit', views.calcprofit, name='calcprofit'),
    path('load_data', views.load_data, name='load_data'), 
    path('save_settings', views.save_settings, name='save_settings'), 
    path('user_login', views.user_login, name='user_login'), 
    path('user_logout', views.user_logout, name='user_logout'), 
    
]