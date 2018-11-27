from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class PreviousReportListView(View):
    template_name = 'previous_reports/previous_reports.html'

    def get(self, request, *args, **kwargs):
        prev_crimes = [
            ('Hacker infestation at MoJ', 'Nov 24', 'Many Franco Manca pizzas ordered.'),
            ('Robbery in Soho', 'Nov 20', 'Criminal identified and manhunt conducted.'),
            ('Assault in Bloomsbury', 'Mar 16', 'Criminal proven guilt in court and jailed.'),
        ]

        context = {
            'prev_crimes': prev_crimes,
        }
        return render(request, template_name=self.template_name, context=context)