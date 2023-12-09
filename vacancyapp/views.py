from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from vacancyapp.utils import *
from vacancyapp.models import *
import random


def view_fucn(request):
    jobs = Job.objects.all()

    paginator = Paginator(jobs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj,
               "paginator": paginator}

    return render(request, "vacancyapp/vacancy_list.html", context=context)


class ViewClass(ListView):
    paginate_by = 3
    template_name = "vacancyapp/vacancy_list.html"
    model = Job


class VacancyDetail(DetailView):
    model = Job
    template_name = 'vacancyapp/vacancy_detail.html'
    context_object_name = 'vacancy'
