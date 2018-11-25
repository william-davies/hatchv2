from django.urls import path
from django.views.generic import TemplateView

from dashboard.views import DashboardView
from previous_reports.views import PreviousReportListView

app_name = 'previous_reports'

urlpatterns = [
    path('', PreviousReportListView.as_view(), name='previous-reports')
]