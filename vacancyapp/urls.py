from django.urls import path
from vacancyapp.views import  *

urlpatterns = [
    path('', view_fucn, name="func"),
    path('class/', ViewClass.as_view(), name="class"),
    path('vacancy/<int:pk>/', VacancyDetail.as_view(), name='vacancy')
]




