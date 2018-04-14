"""welearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from WelearnApp import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('WelearnApp/tutor/', views.tutor_page, name='tutor'),
    path('WelearnApp/problem/', views.problem_page, name='problem'),
    path('WelearnApp/examination/', views.examination_page, name='examination'),
    path('delete_item/<int:item_id>',views.delete_item, name='delete_item'),
    path('delete_comment/<int:comment_id>',views.delete_comment, name='delete_comment'),
    path('WelearnApp/post/', views.post_page, name='post'),
    path('WelearnApp/detail/<int:item_id>', views.detail_page, name='detail'),
]
