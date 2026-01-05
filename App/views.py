from django.shortcuts import render,redirect
from .models import AddQues

def Admin(request):
    if request.method == 'POST':
        category = request.POST.get('cat')
        return redirect(f'/Add/?category={category}')
    return render(request,"Admin.html")

def Add(request):   #AddQst
    category = request.GET.get('category')
    if request.method == 'POST':
        ques = request.POST.get('question')
        op1 = request.POST.get('op1')
        op2 = request.POST.get('op2')
        op3 = request.POST.get('op3')
        op4 = request.POST.get('op4')
        correct_answer =request.POST.get('CorrectAns')
        category = request.POST.get('category')

        if ques and op1 and op2 and op3 and op4:
            AddQues.objects.create(
            Ques=ques,
            op1 = op1,
            op2 = op2,
            op3 = op3,
            op4 = op4,
            correct = correct_answer,
            category = category
            )
    QuestionAndOptions = AddQues.objects.filter(category=category)
    return render(request, 'AddQst.html',{
        'QuestionAndOptions': QuestionAndOptions,
        'category':category #ivde enthin ith venem
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
   category = i.category
   i.delete()
   return redirect(f'/Add/?category={category}')




    
# def User(request):
#     if request.method == 'POST':
#         ques = request.POST.get('question')
#         op1 = request.POST.get('op1')
#         op2 = request.POST.get('op2')
#         op3 = request.POST.get('op3')
#         op4 = request.POST.get('op4')
#         if ques and op1 and op2 and op3 and op4:
#             AddQues.objects.create(
#             Ques=ques,
#             op1 = op1,
#             op2 = op2,
#             op3 = op3,
#             op4 = op4
#             )
#             QuestionAndOptions = AddQues.objects.all()
#     return render(request, 'User.html')
    

# from django.shortcuts import render,redirect
# from .models import Add_Task


# def home(request):
#     if request.method == 'POST' :                   
#         task = request.POST.get('task')             
#         Add_Task.objects.create(task=task)
#         return redirect('home')
    
#     #Retrieve part

#     tasks = Add_Task.objects.all()  #fetch all records from member table

#     #Render the form.html page and send the list of members to display in table
#     return render(request, 'home.html', {'tasks': tasks})

# def update_task(request, id):
#     i = Add_Task.objects.get(id=id)
#     if request.method == 'POST' :
#         i.task = request.POST.get('task')
#         i.save()
#         return redirect('home')
#     return render(request,'update.html',{'i': i})


# def delete_task(request, id):
#     i = Add_Task.objects.get(id=id)
#     i.delete()
#     return redirect('home')

# def strike(text):
#     return ''.join(char + '\u0336' for char in text)
    
# def strike_task(request,id):
#     i = Add_Task.objects.get(id=id)
#     i.task = strike(i.task)
#     i.save()
#     return redirect('home')