from django.urls import path 
from user_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('users/',views.UserList.as_view()),
    path('users/<int:pk>',views.UserDetail.as_view()),
    path('users/<int:pk>/select',views.UserAddService.as_view()),
    path('users/faculty',views.FacultyGroup.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)