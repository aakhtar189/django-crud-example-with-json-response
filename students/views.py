import json

from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q
from django.core import serializers

from students.models import Student
from students.forms import CreateStudentForm, GetRequestForm, GetDeleteForm, GetEditForm, EditStudentForm
from students.utils import create_username
from django.forms.models import model_to_dict


from django.core.urlresolvers import reverse
from django.template.loader import render_to_string


def homepage(request):
    students = Student.objects.all()

    student_detail_content = []
    for student in students:
        student_detail_content.append(
            render_to_string('student/student_detail.html',{
                'student': student
                }, context_instance=RequestContext(request))
            )

    return render_to_response("student/homepage.html",{
        'student_detail_content': student_detail_content,
        'students':students,
        'create_student_form' : CreateStudentForm(),
        'get_request_form' : GetRequestForm(),
        'get_delete_form': GetDeleteForm(),
        'get_edit_form' : GetEditForm(),
        'edit_Student_form' : EditStudentForm(),
    }, context_instance=RequestContext(request))


def create_student(request):

    if request.is_ajax():

        response = {"status": False, "errors": []}

        if request.method == "POST":
            form= CreateStudentForm(request.POST)

            if form.is_valid():
                user = User.objects.create(
                    username=create_username('%s %s' % (form.cleaned_data["first_name"], form.cleaned_data["last_name"])),
                    first_name=form.cleaned_data["first_name"],
                    last_name=form.cleaned_data["last_name"],
                    email=form.cleaned_data["email"],
                )

                student = Student.objects.create(
                    user=user,
                    nationality=form.cleaned_data["nationality"]
                )

                user_id = student.user.id
                user = User.objects.get(id=user_id)

                response["status"] = True

                response["user_info"] = model_to_dict(user, fields=['username', 'first_name', 'last_name', 'email'])

                response["status"] = True

                response["student"] = render_to_string('student/student_detail.html', {
                    'student': student
                }, context_instance=RequestContext(request))

            else:
                for key, value in form.errors.items():
                    tmp = {'key': key, 'error': value.as_text()}
                    response['errors'].append(tmp)

        return HttpResponse(json.dumps(response))


def get_student(request):

    if request.is_ajax():
        response = {"status": False, "user_info":[], "student_info":[], "errors": []}

        if request.method == "POST":
            form = GetRequestForm(request.POST)

            if form.is_valid():

                student = Student.objects.get(
                    user__username = form.cleaned_data["username"]
                )

                user_id = student.user.id
                user = User.objects.get(id=user_id)

                response["status"] = True

                response["user_info"] = model_to_dict(user, fields=['username', 'first_name', 'last_name', 'email'])
                response["student_info"] = model_to_dict(student)
                
            else:
                for key, value in form.errors.items():
                        tmp = {'key': key, 'error': value.as_text()}
                        response['errors'].append(tmp)     

            return HttpResponse(json.dumps(response))


def delete_student(request):

    if request.is_ajax():
    
        response = {"status": False, "errors": []}

        if request.method == "POST":
            form = GetDeleteForm(request.POST)

            if form.is_valid():

                student = Student.objects.get(
                    user__username = form.cleaned_data["username"]
                )

                student.user.delete()
                student_id = student.id

                response["status"] = True
                response["student_deleted"] = model_to_dict(student, fields=['username', 'id'])
                response["status"] = True
                
            else:
                for key, value in form.errors.items():
                        tmp = {'key': key, 'error': value.as_text()}
                        response['errors'].append(tmp)     

            return HttpResponse(json.dumps(response))



def edit_student(request):

    if request.is_ajax():
        response = {"status": False, "errors": []}

        if request.method == "POST":
            form = GetEditForm(request.POST)

            if form.is_valid():

                student = Student.objects.get(
                    user__username = form.cleaned_data["username"]
                )

                response["status"] = True
                user_id = student.user.id
                user = User.objects.get(id=user_id)

                response["status"] = True

                response["student"] = model_to_dict(student, fields=['id', 'nationality'] )

                response["user_info"] = model_to_dict(user, fields=['username', 'first_name', 'last_name', 'email'])
            else:
                for key, value in form.errors.items():
                        tmp = {'key': key, 'error': value.as_text()}
                        response['errors'].append(tmp)

            return HttpResponse(json.dumps(response))



def actual_edit(request, student_id):

    student_id = request.Get.get('student_id', '')

    response = { "status": False, "errors":[] } 

    if request.method == "POST":

        form = EditStudentForm(request.POST)

        if form.is_valid():
            student.user.first_name = form.cleaned_data["first_name"]
            student.user.last_name = form.cleaned_data["last_name"]
            student.user.email = form.cleaned_data["email"]
            student.nationality = form.cleaned_data["nationality"]
            student.save()

            response["status"] = True

            response["student"] = render_to_string('student/student_detail.html', {
                'student': student
            }, context_instance=RequestContext(request))
        else:
            for key, value in form.errors.items():
                tmp = {'key': key, 'error': value.as_text()}
                response['errors'].append(tmp)

    return HttpResponse(json.dumps(response))










