from django.urls import path
from .import views

urlpatterns = [
   path('',views.Admin,name='Admin'),
   path('User/',views.User,name='User'),
   path('Add/', views.Add, name='AddQst'),
   path('TakeQuiz/',views.TakeQuiz,name='TakeQuiz'),
   path('delete/<int:id>/',views.DeleteQues,name='Delete11'),
   path('edit/<int:id>/',views.EditQues,name='Edit11'),
]