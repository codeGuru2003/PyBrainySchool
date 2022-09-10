from django.contrib.auth.models import AbstractUser, UserManager
from datetime import date, datetime
from django.db import models


class GenderTypes(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MyUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    password_hint = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(null=True)
    phone_number = models.IntegerField(null=True)
    address = models.CharField(max_length=200, null=True)
    image = models.ImageField("user_image",null=True)
    gender = models.ForeignKey(GenderTypes,on_delete=models.CASCADE, null=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
class School(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__ (self):
        return self.name

class AcademicSchoolYearType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class AcademicSchoolYear(models.Model):
    academicSchoolYearType = models.ForeignKey(AcademicSchoolYearType,on_delete=models.CASCADE)
    isActive = models.BooleanField()

    def __str__(self):
        return self.academicSchoolYearType.name

class AcademicSemesterType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AcademicSemester(models.Model):
    academicSchoolYear = models.ForeignKey(AcademicSchoolYear, on_delete=models.CASCADE)
    academicSemesterType = models.ForeignKey(AcademicSemesterType, on_delete=models.CASCADE)
    startdate = models.DateTimeField(default = datetime.now)
    enddate = models.DateTimeField()

    def __str__(self):
        return self.AcademicSemesterType.name


class PeriodType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__ (self):
        return self.name


class AcademicSemesterPeriod(models.Model):
    periodType = models.ForeignKey(PeriodType, on_delete=models.CASCADE)
    academicSemester = models.ForeignKey(AcademicSemester, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.periodType.name} {self.academicSemester.name}"



class ClassType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Class(models.Model):
    classType = models.ForeignKey(ClassType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ClassBillingItems(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amountInUSD = models.FloatField()
    amountInLRD = models.FloatField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class NationalityType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__ (self):
        return self.name

class MaritalStatusType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class InstallmentType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class FamilyMemberType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__ (self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__ (self):
        self.name

class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField("image")

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    nationalityType = models.ForeignKey(NationalityType, on_delete=models.CASCADE)

    def __str__ (self):
        return f"{self.user.firstname} {self.user.lastname}"

class StudentClass(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    academicSemester = models.ForeignKey(AcademicSemester, on_delete=models.CASCADE)

    def __str__(self):
        return self.Class.name

class StudentGrade(models.Model):
    studentClass = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    academicSemesterPeriod = models.ForeignKey(AcademicSemesterPeriod, on_delete=models.CASCADE)
    grade = models.FloatField()
    grade_letter = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.grade} {self.grade_letter}"

class Parent(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    is_Alive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.firstname} {self.user.lastname}"

class FamilyMember(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.user.firstname} {self.parent.user.firstname}"

class FacultyType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    faculty_type = models.ForeignKey(FacultyType, on_delete=models.CASCADE)

    def __str__ (self):
        return f"{self.user.firstname} {self.user.lastname} {self.faculty_type.name}"

