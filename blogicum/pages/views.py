from django.shortcuts import render


def about(request):
    template_name = 'pages/about.html'
    return render(request, template_name)


def rules(request):
    template_name = 'pages/rules.html'
    return render(request, template_name)


def travel(request):
    template_name = 'pages/travel.html'
    return render(request, template_name)


def notmyday(request):
    template_name = 'pages/notmyday.html'
    return render(request, template_name)
# Create your views here.
