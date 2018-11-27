from django.urls import path
from django.views.generic import TemplateView


app_name = 'nearby_crimes'

urlpatterns = [
    path('', TemplateView.as_view(template_name='nearby_crimes/nearby_crimes.html'), name='nearby_crimes')
]