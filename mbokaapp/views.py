from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.http import Http404, HttpResponseRedirect

from account.models import User
from jobapp.forms import *
from jobapp.models import *
from jobapp.permission import *
User = get_user_model()


# Create your views here.
def home_view(request):

    jobs = Job.objects.order_by('-timestamp')
    total_candidates = User.objects.filter(role='employee').count()
    total_companies = User.objects.filter(role='employer').count()

    paginator = Paginator(jobs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {

        'total_candidates': total_candidates,
        'total_companies': total_companies,
        'total_jobs': len(jobs),
        'page_obj': page_obj
    }
    return render(request, 'mbokaapp/index.html', context)

def job_list_View(request):

    job_list = Job.objects.order_by('-timestamp')
    paginator = Paginator(job_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {

        'page_obj': page_obj,

    }
    return render(request, 'mbokaapp/job-list.html', context)


@login_required(login_url=reverse_lazy('account:login'))
@user_is_employer
def create_job_View(request):

    form = JobForm(request.POST or None)

    user = get_object_or_404(User, id=request.user.id)
    categories = Category.objects.all()

    if request.method == 'POST':

        if form.is_valid():

            instance = form.save(commit=False)
            instance.user = user
            instance.save()
            # for save tags
            form.save_m2m()

            return redirect(reverse("mbokaapp:single-job", kwargs={
                                    'id': instance.id
                                    }))

    context = {
        'form': form,
        'categories': categories
    }
    return render(request, 'mbokaapp/post-job.html', context)

def single_job_view(request, id):

    job = get_object_or_404(Job, id=id)
    related_job_list = job.tags.similar_objects()

    paginator = Paginator(related_job_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'job': job,
        'page_obj': page_obj,
        'total': len(related_job_list)

    }
    return render(request, 'mbokaapp/job-single.html', context)



def search_result_view(request):

    job_list = Job.objects.order_by('-timestamp')

    # Keywords
    if 'job_title_or_company_name' in request.GET:
        job_title_or_company_name = request.GET['job_title_or_company_name']

        if job_title_or_company_name:
            job_list = job_list.filter(title__icontains=job_title_or_company_name) | job_list.filter(
                company_name__icontains=job_title_or_company_name)

    # location
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            job_list = job_list.filter(location__icontains=location)

    # Job Type
    if 'job_type' in request.GET:
        job_type = request.GET['job_type']
        if job_type:
            job_list = job_list.filter(job_type__iexact=job_type)

    # job_title_or_company_name = request.GET.get('text')
    # location = request.GET.get('location')
    # job_type = request.GET.get('type')

    #     job_list = Job.objects.all()
    #     job_list = job_list.filter(
    #         Q(job_type__iexact=job_type) |
    #         Q(title__icontains=job_title_or_company_name) |
    #         Q(location__icontains=location)
    #     ).distinct()

    # job_list = Job.objects.filter(job_type__iexact=job_type) | Job.objects.filter(
    #     location__icontains=location) | Job.objects.filter(title__icontains=text) | Job.objects.filter(company_name__icontains=text)

    paginator = Paginator(job_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {

        'page_obj': page_obj,

    }
    return render(request, 'mbokaapp/result.html', context)


