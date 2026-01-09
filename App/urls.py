from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   # path('',views.home,name='home'),
   path('',views.Admin,name='Admin'),
   path('User/',views.User,name='User'),
   path('Reg/',views.UserReg,name='UserReg'),
   path('Add/', views.Add, name='AddQst'),
   path('TakeQuiz/',views.TakeQuiz,name='TakeQuiz'),
   path('delete/<int:id>/',views.DeleteQues,name='Delete11'),
   path('edit/<int:id>/',views.EditQues,name='EditQues'),
   path('DeleteCat/<int:id>/', views.DeleteCat, name='DeleteCat'),
   path('UpdateCat/<int:id>/', views.UpdateCat, name='UpdateCat'),
   path('UpdateUser/<int:id>/', views.UpdateUser, name='UpdateUser'),
   path('DisplayUser/<int:id>/', views.DisplayUser, name='DisplayUser'),
   path('Login/', views.UserLogin, name='UserLogin'),
   path('Logout/', views.UserLogout, name='UserLogout')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)