from django.urls import path
from .views import InquiryAPI,TestDriveAPI,ContactAPI
from cars.views import BlogAPI

urlpatterns = [
    path('enquiry',InquiryAPI.as_view()),
    path('enquiry/<str:pk>',InquiryAPI.as_view()),
    
    path('test-drive',TestDriveAPI.as_view()),
    path('test-drive/<str:pk>',TestDriveAPI.as_view()),
    
    path('contact',ContactAPI.as_view()),
    path('contact/<str:pk>',ContactAPI.as_view()),
    
    path('blog',BlogAPI.as_view()),
    path('blog/<str:pk>',BlogAPI.as_view()),
]