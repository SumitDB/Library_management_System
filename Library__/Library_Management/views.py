from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from Library_Management.models import Book, IssuedBook, Student
from Library_Management.serializer import BookSerializer, StudentSerializer, IssuedBooksSerializer

from rest_framework.views import APIView
# Create your views here.
class BookList(APIView):
    def get(self, request):
        book =Book.objects.all() 
        serializer =BookSerializer(book, many=True)
        return Response(serializer.data)

class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BookDetial(APIView):
    def get_book_by_pk(self, pk):
        try:
            book = Book.objects.get(id=pk)
        except:
            return Response({
            'error':'Book does not exist'
        }, status = status.HTTP_404_NOT_FOUND)
         
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        book = Book.objects.get(id=pk)
        book.delete()
        return Response(status.HTTP_204_NO_CONTENT)

class Studentlist(APIView):
    def get(self,request):
        student =Student.objects.all()
        serializer =StudentSerializer(student, many=True)
        return Response(serializer.data)

class StudentCreate(APIView):
    def post(self, request):
        serializer= StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
class StudentOP(APIView):
    def get_student_by_roll_no(self, pk):
        try:
            student = Student.objects.get(id=pk)
        except:
            return Response({
            'error':'Student does not exist'
        }, status = status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        student  = Student.objects.get(id=pk)
        student.delete()
        return Response(status.HTTP_204_NO_CONTENT)
