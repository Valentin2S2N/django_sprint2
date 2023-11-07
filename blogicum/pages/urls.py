from django.urls import path

from . import views

app_name = 'pages'

# Не забыть добваить это в шаблон html namespace:name

urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
    path('travel/', views.travel, name='travel'),
    path('notmyday/', views.notmyday, name='notmyday'),
]
