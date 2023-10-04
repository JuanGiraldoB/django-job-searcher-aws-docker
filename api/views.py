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


class JobsByCategoryView(View):
    template_name = 'api/jobs_by_category.html'
    api = GetOnBoardAPI()

    def get_context_data(self, category_id):
        context = {}
        context['category'] = category_id

        # Access the filter criteria from the request.GET dictionary
        min_salary = self.request.GET.get('min_salary')

        # Query the jobs based on the filter criteria
        jobs = self.api.get_jobs(category=category_id)['data']

        # Apply salary filter if criteria are provided

        filtered_jobs = self.filter_jobs_min_salary(jobs, min_salary)

        if filtered_jobs:
            context['jobs'] = filtered_jobs
        else:
            context['jobs'] = jobs

        return context

    def get(self, request, category_id, *args, **kwargs):
        context = self.get_context_data(category_id)
        return render(request, self.template_name, context)

    def filter_jobs_min_salary(self, jobs, min_salary):
        filtered_jobs = []

        if min_salary:
            min_salary = float(min_salary)

            for job in jobs:
                job_min_salary = job['attributes']['min_salary']

                if not job_min_salary:
                    continue

                if job_min_salary < min_salary:
                    continue

                filtered_jobs.append(job)

        return filtered_jobs
