from django.shortcuts import render,redirect,get_object_or_404
from .models import AddQues,AddCategory,UserRegister,UserScore
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password

# def home(request):
#     if request.user.is_authenticated and request.user.is_superuser:
#         # Superuser → go to Django admin panel
#         return redirect('/admin/')
#     elif request.session.get('user_id'):
#         # Normal user → logged in via your UserRegister system
#         return redirect('User')
#     else:
#         # Not logged in → go to registration page
#         return redirect('UserReg')

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
    
    cat_obj = get_object_or_404(AddCategory, CategoryName=category)
    QuestionAndOptions = AddQues.objects.filter(category=cat_obj)
    totalQuestions = QuestionAndOptions.count()
    score = None
    CorrectAns = {}

    user_id = request.session.get('user_id')  # store this when user logs in
    if not user_id:
        return redirect('UserReg')  # force registration/login
    user = get_object_or_404(UserRegister, id=user_id)

    if request.method=='POST':
        score = 0
        for i in QuestionAndOptions:
            UserAns = request.POST.get(str(i.id))
            CorrectAns[i.id] = i.correct
            if UserAns == i.correct :
                score += 1
        user = request.user

        UserScore.objects.create(
            user = user,
            category = cat_obj,
            score = score,
            total_questions=totalQuestions
        )

            
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


def EditQues(request,id):
    category = request.GET.get('category') or request.POST.get('category')
    if not category:
        return redirect('Add')
    
    cat_obj = get_object_or_404(AddCategory, CategoryName=category)
    i = AddQues.objects.get(id=id)

   
    if request.method=='POST':
        i.Ques = request.POST.get('question')
        i.op1 = request.POST.get('op1')
        i.op2 = request.POST.get('op2')
        i.op3 = request.POST.get('op3')
        i.op4 = request.POST.get('op4')

       

        i.correct = request.POST.get('CorrectAns')
        i.save()   
        return redirect(f'/Add/?category={category}')
    return render(request, 'update.html',{
        'i' : i
    })

def DeleteCat(request, id):
    category = get_object_or_404(AddCategory, id=id)
    category.delete()
    return redirect('Admin') 

def UpdateCat(request, id):
    category = get_object_or_404(AddCategory, id=id)

    if request.method == 'POST':
        category.CategoryName = request.POST.get('CatName')
        category.CategoryDescription = request.POST.get('CatDes')
        category.save()
        return redirect('Admin')

    return render(request, 'UpdateCat.html', {
        'category': category
    })


def UserReg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        education = request.POST.get('education')
        dob = request.POST.get('dob')
        photo = request.FILES.get('photo')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # password match check
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('UserReg')

        # email already exists check
        if UserRegister.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('UserReg')

        user = UserRegister(
            name=name,
            email=email,
            education=education,
            dob=dob,
            photo=photo,
            password=make_password(password)  # password hashed
        )
        user.save()
        request.session['user_id'] = user.id

        print("Redirecting to User page...")
        messages.success(request, "Registration successful")
        return redirect('User')
    return render(request, 'UserReg.html')

def UpdateUser(request, id):
    i = get_object_or_404(UserRegister, id=id)

    if request.method == 'POST':
        i.name = request.POST.get('name')
        i.email = request.POST.get('email')
        i.education = request.POST.get('education')
        i.dob = request.POST.get('dob')

        
        if request.FILES.get('photo'):
            i.photo = request.FILES.get('photo')

        i.save()
        return redirect('Admin')

    return render(request, 'edit_user.html', {
        'i': i
    })

def DisplayUser(request, id):
    i = get_object_or_404(UserRegister, id=id)
    return render(request, 'DisplayUser.html', {
        'user': i
    })

def UserLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserRegister.objects.get(email=email)
            if check_password(password, user.password):
                # Save user in session
                request.session['user_id'] = user.id
                messages.success(request, f"Welcome back, {user.name}!")
                return redirect('User')  # go to user dashboard
            else:
                messages.error(request, "Incorrect password")
        except UserRegister.DoesNotExist:
            messages.error(request, "User not found. Please register first.")
        
        return redirect('UserLogin')
    
    return render(request, 'UserLogin.html')


# LOGOUT
def UserLogout(request):
    request.session.flush()  # remove all session data
    messages.success(request, "Logged out successfully")
    return redirect('UserLogin')