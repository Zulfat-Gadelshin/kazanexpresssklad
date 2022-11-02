from django.urls import path
from . import views

app_name = 'tovary_url'

urlpatterns = [
    path('all', views.tovary, name='tovary'),
    path('new_tovar', views.new_tovar, name='new_tovar'),
    path('zagruzka_prodag', views.zagruzka_prodag, name='zagruzka_prodag'),

]
