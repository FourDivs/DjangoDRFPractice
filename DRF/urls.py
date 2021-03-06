"""DRF URL Configuration

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
# from restApp.views import student_detail, student_list
# from restApp.views_class_based import StudentList, StudentDetail
# from restApp.views_mixins import StudentList, StudentDetail
# from restApp.views_generic_api_views import StudentList, StudentDetail
from restApp.views_viewsets import StudentViewSet
from rest_framework.routers import DefaultRouter  # type: ignore

router = DefaultRouter()
router.register('students', StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('students/', student_list, name='student_list'),
    # path('students/<int:pk>', student_detail, name='student_detail'),
    # path('students/', StudentList.as_view(), name='student_list'),
    # path('students/<int:pk>', StudentDetail.as_view(), name='student_detail')
    path('', include(router.urls))
]
