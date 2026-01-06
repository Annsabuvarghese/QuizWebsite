from django.shortcuts import render,redirect,get_object_or_404
from .models import AddQues,AddCategory

def Admin(request):
    if request.method == 'POST':
        category = request.POST.get('CatName')
        Description = request.POST.get('CatDes')

        # CASE-INSENSITIVE check
        if not AddCategory.objects.filter(CategoryName__iexact=category).exists():
            AddCategory.objects.create(
                CategoryName=category,
                CategoryDescription=Description
                )
            
            
        return redirect('Admin')
    CatNameDes = AddCategory.objects.all()
    return render(request,'Admin.html',{
        'NamesDes' : CatNameDes
    })



def Add(request):   #AddQst
    category_name= request.GET.get('category') or request.POST.get('category')
    if not category_name:
        return redirect('Admin')
    
    cat = get_object_or_404(AddCategory, CategoryName__iexact=category_name)
    if request.method == 'POST':
        ques = request.POST.get('question')
        op1 = request.POST.get('op1')
        op2 = request.POST.get('op2')
        op3 = request.POST.get('op3')
        op4 = request.POST.get('op4')
        correct_answer =request.POST.get('CorrectAns')
        

        if ques and op1 and op2 and op3 and op4 and correct_answer:
            AddQues.objects.create(
            Ques=ques,
            op1 = op1,
            op2 = op2,
            op3 = op3,
            op4 = op4,
            correct = correct_answer,
            category = cat
            )
        return redirect(f'/Add/?category={category_name}')

    QuestionAndOptions = AddQues.objects.filter(category=cat)
    return render(request, 'AddQst.html',{
        'QuestionAndOptions': QuestionAndOptions,
        'category':category_name #ivde ith venem
    })

def User(request):
    categoryandes = AddCategory.objects.all()
    category = None

    if request.method == 'POST':
        category = request.POST.get('cat')
    if category:
        return redirect(f'/TakeQuiz/?category={category}')
    return render(request,'User.html',{
        'catinfo': categoryandes

    })

def TakeQuiz(request):
    category = request.GET.get('category') or request.POST.get('category')
    if not category:
        return redirect('User')
    
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


