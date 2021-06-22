from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import all_activity,Permission
from time import sleep
from django.core.paginator import Paginator


from .models import Question
def index(request):
    question_set=Question.objects.all()
    permission=Permission.objects.all()


    print(len(question_set))
    for i in permission:
        visible_modified=int(i.visible)
   # li=[]
    if request.method =="POST":
        if visible_modified==1:
            sleep(3)
        li=[]
        for question in question_set:
            nam = request.POST.get(question.name)
            #nam=request.POST
            #print('the value of name is')
            # print(nam)
            li.append(nam)
            #all = all_activity(full =nam ,question=question)
            #all.save();
        all = all_activity(full=li, question=question)
        all.save();

        #print((li))


        return redirect('/home/')

    paginator = Paginator(question_set, 8)
    page = request.GET.get('page')
    question_set = paginator.get_page(page)

    # return render(request,'index.html', {'question_set':question_set,'answer_set':answer_set,'permission':visible_modified})
    return render(request,'FIB.html', {'question_set':question_set,'permission':visible_modified})

def home(request):
    return render(request,'home.html')

def add_show(request):
    question_set = Question.objects.all()
    if request.method == "POST":
        ques = request.POST.get('question')
        ans = request.POST.get('answer')
        ques_name = request.POST.get('question_name')
        all = Question(question=ques, name=ques_name, Currect_ans=ans)
        all.save()
    return render(request,'create_question.html',{'question_set':question_set})

def update_question(request,id):
    question_set = Question.objects.get(pk=id)
    if request.method == 'POST':
        ques = request.POST.get('question')
        ans = request.POST.get('answer')
        ques_name = request.POST.get('question_name')
        all = Question(id=id,question=ques, name=ques_name, Currect_ans=ans)
        all.save()
        return HttpResponseRedirect('/add_show/')

    return render(request,'update_question.html',{'question_set':question_set})

#this is the delete fun.
def delete_question(request,id):
    if request.method=='POST':
        question_set = Question.objects.get(pk=id)
        question_set.delete()
        return HttpResponseRedirect('/add_show/')
