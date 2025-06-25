from django.urls import path
from . import views
urlpatterns = [
path('homepage/<int:id>', views.homePage),
path('aboutus', views.aboutUs),
path('studentform',views.student_form)
]