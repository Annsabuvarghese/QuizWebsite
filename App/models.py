from django.db import models

class AddCategory(models.Model):
    name = models.CharField(max_length=100,unique=True,default='python')

    def __str__(self):
        return self.name

class AddQues(models.Model):
    Ques = models.TextField()
    op1 = models.CharField(max_length=300)
    op2 = models.CharField(max_length=300)
    op3 = models.CharField(max_length=300)
    op4 = models.CharField(max_length=300)
    correct =models.CharField(max_length=300,default='op1')
    category = models.ForeignKey(AddCategory,on_delete = models.CASCADE)

# class UserReg(models.Model):
#     name = models.CharField(max_length=200)
#     age= models.CharField(max_length=3)
#     email =models.EmailField(max_length=300)
#     password = models.CharField(max_length=300)
    