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
    #-----------------------------Tutor-----------------------------------------------------------
    #Tutor Page
    path('WelearnApp/tutor/', views.tutor_page, name='tutor'),
    #page for create post (Tutor Page)
    path('WelearnApp/tutor/post/', views.post_page, name='post'),
    #show detail (Tutor Page)
    path('WelearnApp/tutor/detail/<int:item_id>', views.detail_page, name='detail'),
    #Delete Topic
    path('delete_item/<int:items_id>',views.delete_item, name='delete_item'),
    #Delate comment
    path('delete_comment/<int:comment_id>',views.delete_comment, name='delete_comment'),
    #------------------------Examination----------------------------------------------------------
    #Examination Page
    path('WelearnApp/examination/', views.examination_page, name='examination'),
    #page for create post (Examination Page)
    path('WelearnApp/examination/post/', views.post_exam_page, name='post_exam'),
    #show detail (Examination Page)
    path('WelearnApp/examination/detail/<int:itemExam_id>', views.detail_exam_page, name='detail_exam'),
    #Delete Topic
    path('examination/delete_item/<int:itemsExam_id>',views.delete_exam_item, name='delete_exam_item'),
    #Delate comment
    path('examination/delete_comment/<int:comment_exam_id>',views.delete_exam_comment, name='delete_exam_comment'),
    #----------------------about page-------------------------------------------------------------------------------------------
    path('WelearnApp/about/', views.about, name='about'),
    #path('WelearnApp/test/', views.test, name='test'),
]
