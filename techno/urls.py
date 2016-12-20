from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'students.views.homepage', name='homepage'),
    url(r'student/', include('students.urls')),
]
