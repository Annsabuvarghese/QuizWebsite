from django.db import models


class AddCategory(models.Model):
    CategoryName = models.CharField(max_length=100,unique=True,default='python')
    CategoryDescription = models.TextField(default="This is a computer programming language")

    def __str__(self):
        return self.CategoryName

class AddQues(models.Model):
    Ques = models.TextField()
    op1 = models.CharField(max_length=300)
    op2 = models.CharField(max_length=300)
    op3 = models.CharField(max_length=300)
    op4 = models.CharField(max_length=300)
    correct =models.TextField(max_length=300,default='op1')
    category = models.ForeignKey(AddCategory,on_delete = models.CASCADE)

class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    education = models.CharField(max_length=150)
    dob = models.DateField()
    photo = models.ImageField(upload_to='profile_photos/')
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name
    