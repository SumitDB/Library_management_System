
from rest_framework import serializers
from Library_Management.models import Book , IssuedBook, Student
from django.forms import ValidationError 

class BookSerializer(serializers.ModelSerializer):
    description=serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields= "__all__"
    def validate_name(self,value):
        if value== "Diet Coke":
            raise ValidationError("No diet coke please")
        return value

    def validate(self, data):
        if data["pages"] > 200:
            raise ValidationError("Too heavy for inventroy")
        return data
    def get_description(self, data):
        return "This book is called " +  data.name + " and it is " + str(data.pages) + " pages thick."
    
class IssuedBooksSerializer(serializers.Serializer):
    class Meta:
        model = IssuedBook
        fields = "__all__"
  
class StudentSerializer(serializers.Serializer):
    class Meta:
        model = Student
        fields = "__all__"
    def get_description(self, data):
        return "The Name of student is " +  data.first_name + " and surname is " + data.last_name


    
