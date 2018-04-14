from django.http import HttpResponse
from django.shortcuts import redirect, render
from WelearnApp.models import Topic,Comment
from django.shortcuts import get_list_or_404, get_object_or_404

def home_page(request):
    return render(request, 'home.html')


def tutor_page(request):
    if request.method == 'POST':
        Topic.objects.create(post_text=request.POST.get('post_tutor_head', ''), 
           detail=request.POST.get('post_tutor_detail', ''))
        return redirect('/WelearnApp/tutor/')
    items = Topic.objects.all()
    return render(request, 'tutor.html', {'items': items})

def post_page(request):
     return render(request, 'post.html')
    
def delete_item(request, item_id):
    del_post = Topic.objects.get(id=item_id)
    del_post.delete()
    return redirect('/WelearnApp/tutor/')

def delete_comment(request, comment_id):
    del_comment = Comment.objects.get(id=comment_id)
    del_comment.delete()
    return redirect('/WelearnApp/tutor/')
    #return redirect('/WelearnApp/detail/' + str(comment_id))

def examination_page(request):
    return render(request, 'examination.html')

def problem_page(request):
    return render(request, 'problem.html')

def detail_page(request, item_id):
    #เลือก id กระทู้
    items = Topic.objects.get(id=item_id)
    if request.method == 'POST':
        #creat comment
        Comment.objects.create(cm=request.POST['post_comment'],comment=items)        
        return redirect('/WelearnApp/detail/' + str(items.id))
    #เก็บ comment
    l_comment = Comment.objects.all()    
    return render(request, 'detail.html', {'items': items,'l_comment':l_comment})

