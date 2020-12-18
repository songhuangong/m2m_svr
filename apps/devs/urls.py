from django.conf.urls import url
from django.urls import path

from apps.devs.views import DevListView, DevDetailView, # CourseLessonView  , CourseDetailView, , CourseCommentsView
# from apps.courses.views import VideoView


urlpatterns = [
    url(r'^list/$', DevListView.as_view(), name="list"),
    url(r'^(?P<dev_id>\d+)/$', DevDetailView.as_view(), name="detail"),
]
