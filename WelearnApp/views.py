from django.shortcuts import render

def home_page(request):
  return render(request, 'home.html')


def test_tutor(request):
    return render(request, 'tutor.html')

def test_examination(request):
    return render(request, 'examination.html')

def test_problem(request):
    return render(request, 'problem.html')
