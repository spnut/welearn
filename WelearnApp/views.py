from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from WelearnApp.models import Topic,Comment,TopicExam,Comment_Exam,Profile
from django.shortcuts import get_list_or_404, get_object_or_404

from WelearnApp.forms import ProfileForm
#welcome to welearn and show 2 button(Tutor, Examination)
def home_page(request):
    return render(request, 'home.html')


#----------------------------about page------------------------------------------------------------------
def about(request):
    return render(request, 'about.html')


#----------------------------Tutor-----------------------------------------------------------------------
#Tutor Page show all topic
def tutor_page(request):
    if request.method == 'POST':
        Topic.objects.create(post_text=request.POST.get('post_tutor_head', ''), 
           detail=request.POST.get('post_tutor_detail', ''))
        return redirect('/WelearnApp/tutor/')
    items = Topic.objects.all()
    return render(request, 'tutor.html', {'items': items})

#page for create post (Tutor Page)
def post_page(request):
     return render(request, 'post.html')

#show detail of Topic in tutor page
def detail_page(request, item_id):
    #เลือก id กระทู้
    items = Topic.objects.get(id=item_id)
    if request.method == 'POST':
        #creat comment
        Comment.objects.create(cm=request.POST['post_comment'],comment=items)        
        return redirect('/WelearnApp/tutor/')    
    #เก็บ comment
    l_comments = Comment.objects.all().filter(comment_id=item_id)    
    return render(request, 'detail.html', {'items': items,'l_comments':l_comments})
    
#delate topic
def delete_item(request, items_id):
    if request.method == 'POST':
        Topic.objects.filter(id=items_id).delete()
    '''del_post = Topic.objects.get(id=items_id)
    del_post.delete()'''
    return redirect('/WelearnApp/tutor/')
#delate comment
def delete_comment(request, comment_id):
    if request.method == 'POST':
        Comment.objects.filter(id=comment_id).delete()
    '''del_comment = Comment.objects.get(id=comment_id)
    del_comment.delete()'''
    return redirect('/WelearnApp/tutor/')



#--------------------Examination-----------------------------------------------------------
#Examination Page show all topic
def examination_page(request):
    if request.method == 'POST':
        TopicExam.objects.create(topic_exam=request.POST.get('post_exam_head', ''), 
           detail_exam=request.POST.get('post_exam_detail', ''))
        return redirect('/WelearnApp/examination/')
    itemsExam = TopicExam.objects.all()
    return render(request, 'examination.html', {'itemsExam': itemsExam})

#page for create post (Tutor Page)
def post_exam_page(request):
     return render(request, 'post_exam.html')

#show detail of Topic in examination page
def detail_exam_page(request, itemExam_id):
    #เลือก id กระทู้
    itemsExam = TopicExam.objects.get(id=itemExam_id)
    if request.method == 'POST':
        #creat comment
        Comment_Exam.objects.create(cm_exam=request.POST['post_comment'],comment_exam=itemsExam)        
        return redirect('/WelearnApp/examination/')
    #เก็บ comment
    commentsExam = Comment_Exam.objects.all().filter(comment_exam=itemExam_id)    
    return render(request, 'detail_exam.html', {'itemsExam': itemsExam,'commentsExam':commentsExam})

#delate topic
def delete_exam_item(request, itemsExam_id):
    TopicExam.objects.filter(id=itemsExam_id).delete()
    '''del_post = Topic.objects.get(id=items_id)
    del_post.delete()'''
    return redirect('/WelearnApp/examination/')
#delate comment
def delete_exam_comment(request, comment_exam_id):
    Comment_Exam.objects.filter(id=comment_exam_id).delete()
    '''del_comment = Comment.objects.get(id=comment_id)
    del_comment.delete()'''
    return redirect('/WelearnApp/examination/')
    #return redirect('/WelearnApp/detail/' + str(comment_id))




#---------------------------Test Uplodefile-------------------------------
'''def SaveProfile(request):
    saved = False

    if request.method == "POST":
        MyProfileForm = ProfileForm(request.POST, request.FILES)

        if MyProfileForm.is_valid():
            profile = Profile()
            profile.title = MyProfileForm.cleaned_data["title"]
            profile.filePic = MyProfileForm.cleaned_data["filePic"]
            profile.save()

            saved = True
    else:
        MyProfileForm = ProfileForm()

    return render(request, 'saved.html', locals())

def Profile(request):
    return render(request, 'profile.html')'''