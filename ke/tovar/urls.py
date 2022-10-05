from django.urls import path
from . import views

app_name = 'tovary_url'

urlpatterns = [
    path('all', views.TovaryViewSet.as_view, name='tovary'),
    path('new_tovar', views.new_tovar, name='new_tovar'),

    ]
