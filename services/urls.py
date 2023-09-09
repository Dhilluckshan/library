from django.urls import path 
from services import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('services/',views.ServiceList.as_view()),
    path('services/<int:pk>',views.ServiceDetail.as_view()),
    path('services/count',views.ServiceCountView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)