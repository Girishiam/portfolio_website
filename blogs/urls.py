from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('',views.blogs,name='blogs'),
    path('<int:blog_id>/', views.details, name='details')
]