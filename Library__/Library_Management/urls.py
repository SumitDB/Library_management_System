
from django.urls import path
from Library_Management.views import BookList, BookCreate, BookDetial
from Library_Management.views import Studentlist, StudentCreate, StudentOP

urlpatterns = [
    path('bookcreate/', BookCreate.as_view()),
    path('booklist/', BookList.as_view()),
    path('bookdetail/<int:pk>/',BookDetial.as_view()),
    path('studentcreate/', StudentCreate.as_view()),
    path('studentlist/', Studentlist.as_view()),
    path('studentdetail/<int:pk>/',StudentOP.as_view()),
]