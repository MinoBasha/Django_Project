from django.urls import path

from . import views
app_name = 'libraryApp'

urlpatterns = [
	path('',views.listWriters,name='writers'),

]