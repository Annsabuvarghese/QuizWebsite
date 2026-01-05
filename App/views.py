from django.shortcuts import render,redirect
from .models import AddQues,AddCategory

def Admin(request):
    if request.method == 'POST':
        category = request.POST.get('CatName')
        Description = request.POST.get('CatDes')
        if category and Description:
            AddCategory.objects.create(
                CategoryName = category,
                CategoryDescription = Description
            )
            
        return redirect(f'/Add/?category={category}')
    CatNameDes = AddCategory.objects.all()
    return render(request,'Admin.html',{
        'NamesDes' : CatNameDes
    })



def Add(request):   #AddQst
    category_name= request.GET.get('category') or request.POST.get('category')
    cat = AddCategory.objects.get(CategoryName='category') 
    if request.method == 'POST':
        ques = request.POST.get('question')
        op1 = request.POST.get('op1')
        op2 = request.POST.get('op2')
        op3 = request.POST.get('op3')
        op4 = request.POST.get('op4')
        correct_answer =request.POST.get('CorrectAns')
        

        if ques and op1 and op2 and op3 and op4:
            AddQues.objects.create(
            Ques=ques,
            op1 = op1,
            op2 = op2,
            op3 = op3,
            op4 = op4,
            correct = correct_answer,
            category = cat
            )
    QuestionAndOptions = AddQues.objects.filter(category=cat)
    return render(request, 'AddQst.html',{
        'QuestionAndOptions': QuestionAndOptions,
        'category':category_name #ivde enthin ith venem
    })

def User(request):
    if request.method == 'POST':
        category = request.POST.get('cat')
        return redirect(f'/TakeQuiz/?category={category}')
    return render(request,"User.html")

def TakeQuiz(request):
    category = request.GET.get('category') or request.POST.get('category')
    QuestionAndOptions = AddQues.objects.filter(category=category)
    totalQuestions = QuestionAndOptions.count()
    score = None
    CorrectAns = {}

    if request.method=='POST':
        score = 0
        for i in QuestionAndOptions:
            UserAns = request.POST.get(str(i.id))
            CorrectAns[i.id] = i.correct
            if UserAns == i.correct :
                score += 1
            
   

    return render(request, 'Quiz.html',{
        'QuestionAndOptions': QuestionAndOptions,
        'score' : score,
        'totalQ' : totalQuestions,
        'Ans' : CorrectAns,
        'category':category
    })

def DeleteQues(request, id):
   i = AddQues.objects.get(id=id)
   category = i.category.CategoryName
   i.delete()
   return redirect(f'/Add/?category={category}')


