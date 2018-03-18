from django.http import HttpResponse
from django.shortcuts import redirect, render
from WelearnApp.models import Item

def home_page(request):
    return render(request, 'home.html')


def test_tutor(request):
    if request.method == 'POST':
        Item.objects.create(post_text=request.POST['post_tutor_item'])
        return redirect('/WelearnApp/tutor/')
    items = Item.objects.all()
    return render(request, 'tutor.html', {'items': items})
    #return render(request, 'tutor.html', {'A_new_post' : request.POST.get('post_item',''),})
    # post_item, A_new_post is variable in tutor.html

'''def test_tutor_post(request):
    # 'post_tutor_item' is name inputbox form tutorpost.html
    if request.method == 'POST':
        Item.objects.create(text=request.POST['post_tutor_item'])
        return redirect('/WelearnApp/tutor/post')
    items = Item.objects.all()
    return render(request, 'tutorpost.html', {'items': items})'''

'''def test_comment(request):
    if request.method == 'POST':
        first_item = Item()
        #a = first_item(id=id) 
        Item.objects.create(text=request.POST['id_new_post_tutor'], comment=request.POST['name_tutor_comment_post'])
        return redirect('/WelearnApp/tutor/post/comment')
    items = Item.objects.all()
    return render(request, 'comment.html', {'items': items})'''

def delete_item(request, item_id):
    del_post = Item.objects.get(id=item_id)
    del_post.delete()
    return redirect('/WelearnApp/tutor/')


    '''item = Item()
    item.text = request.POST.get('post_tutor_item','')
    item.save()

    return render(request, 'tutorpost.html', {
        'A_new_tutor_post' : item.text })'''

def test_examination(request):
    return render(request, 'examination.html')

def test_problem(request):
    return render(request, 'problem.html')

