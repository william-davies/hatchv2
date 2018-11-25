from django.urls import path
from django.views.generic import TemplateView

from dashboard.views import DashboardView

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(template_name='dashboard/dashboard.html'), name='dashboard')
]