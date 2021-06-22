from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/',views.home,name='home'),
    path('add_show/',views.add_show,name='add_show'),
    path('delete/<int:id>/',views.delete_question,name='delete_question'),
    path('update_question/<int:id>',views.update_question,name='update_question'),
]
