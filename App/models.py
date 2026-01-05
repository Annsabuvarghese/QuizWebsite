from django.db import models

# Create your models here.
# class Add_Task(models.Model):
#     task = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.task


class AddQues(models.Model):
    Ques = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=300)
    op2 = models.CharField(max_length=300)
    op3 = models.CharField(max_length=300)
    op4 = models.CharField(max_length=300)
    correct =models.CharField(max_length=300,default='op1')
    category = models.CharField(max_length=200,default='python')

class UserReg(models.Model):
    name = models.CharField(max_length=200)
    age= models.CharField(max_length=3)
    email =models.EmailField(max_length=300)
    
    