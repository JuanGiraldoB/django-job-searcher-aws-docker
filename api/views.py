from django.shortcuts import render
from django.views import View
from .get_on_board_api import GetOnBoardAPI


class GetOnBoardListView(View):
    template_name = 'api/getonboard.html'
    api = GetOnBoardAPI()

    def get_context_data(self):
        context = {}
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)


class JobListView(GetOnBoardListView):
    def get_context_data(self):
        context = super().get_context_data()
        context['jobs'] = self.api.get_jobs()['data']
        return context


class CategoryListView(GetOnBoardListView):
    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = self.api.get_categories()['data']
        return context


class CompanyListView(GetOnBoardListView):
    def get_context_data(self):
        context = super().get_context_data()
        context['companies'] = self.api.get_companies()['data']
        return context


class JobsByCategoryView(View):
    template_name = 'api/jobs_by_category.html'
    api = GetOnBoardAPI()

    def get_context_data(self, category_id):
        context = {}
        context['jobs'] = self.api.get_jobs(category=category_id)
        context['category'] = category_id.capitalize()
        return context

    def get(self, request, category_id, *args, **kwargs):
        context = self.get_context_data(category_id)
        return render(request, self.template_name, context)
