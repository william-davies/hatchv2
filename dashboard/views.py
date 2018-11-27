from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class DashboardView(View):
    template_name = 'dashboard/dashboard.html'

    def get(self, request, *args, **kwargs):
        img_list = [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
        context = {
            'img_list': img_list,
        }
        return render(request, template_name=self.template_name, context=context)