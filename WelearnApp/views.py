from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')


def test_tutor(request):
    return render(request, 'tutor.html')
    #return render(request, 'tutor.html', {'A_new_post' : request.POST.get('post_item',''),})
    # post_item, A_new_post is variable in tutor.html

def test_examination(request):
    return render(request, 'examination.html')

def test_problem(request):
    return render(request, 'problem.html')

def test_home_post(request):
    return render(request, 'homepost.html')

def test_tutor_post(request):
    return render(request, 'tutorpost.html', {'A_new_tutor_post' : request.POST.get('post_tutor_item',''),})