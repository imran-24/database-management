"""SEAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings 
from django.conf.urls.static import static 
from seasapp import populations,views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('update/',populations.upload_file,name='update'),
    path('home/',views.home,name='home'),
    path('success/',views.success),

    path('classroom/',views.classroom,name='classroom'),
    path('classroomTable/',views.classroom_requirement),

    path('course_distribution/',views.course_distribution,name='course_distribution'),
    path('course_distribution_view/',views.Enrollment_wise_course_distribution),
   
    path('resource_usage/',views.resource_usage,name='resource_usage'),
    path('resource_usage_view/',views.usage_of_resource),

    path('available_resource/',views.available_resource,name='available_resource'),

    path('availability_course_offering/',views.Availability_course_offering,name='availability_course_offering'),
    path('availability_course_offering_view/',views.Availability_course_offering_comparison),

    path('revenue/',views.IUB_revenues,name='revenue'),
    path('revenue_view/',views.revenue_of_IUB),

    path('engineering_school_revenue/',views.engineering_school,name='engineering_school'),
    path('engineering_school_revenue_view/',views.revenue_in_engineering_school),

   
    
    path('register/',user_views.register,name='register'), 
    path('profile/',user_views.profile,name='profile'),
    path('login/', auth_views. LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]


if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 