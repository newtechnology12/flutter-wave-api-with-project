from django.urls import path

from course import views as course_views


urlpatterns = [
	#Leave as empty string for base url
	
	path('', course_views.custom_payment, name="course"),

]