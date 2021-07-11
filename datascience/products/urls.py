from django.urls import path
from .views import Chartselectview
app_name = 'products'

urlpatterns = [
    path('chart/', Chartselectview, name='chart_select_view'),
]