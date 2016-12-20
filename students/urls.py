from django.conf.urls import url 

urlpatterns = [
    url(r'^create-student/$', 'students.views.create_student', name='create_student'),
    url(r'^get-student/$', 'students.views.get_student', name='get_student'),
    url(r'^delete-student/$', 'students.views.delete_student', name='delete_student'),
    url(r'^edit-student/$', 'students.views.edit_student', name='edit_student'),
    url(r'^edit-actual-student/$', 'students.views.actual_edit', name='actual_edit'),
]
