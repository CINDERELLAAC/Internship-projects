from rest_framework import viewsets
from .models import Instructor, Student, Course, Enrollment
from .serializers import InstructorSerializer, StudentSerializer, CourseSerializer, EnrollmentSerializer

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        category = self.request.query_params.get('category')
        instructor = self.request.query_params.get('instructor')
        difficulty_level = self.request.query_params.get('difficulty_level')

        if category:
            queryset = queryset.filter(category=category)
        if instructor:
            queryset = queryset.filter(instructor__name=instructor)
        if difficulty_level:
            queryset = queryset.filter(difficulty_level=difficulty_level)

        return queryset

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
