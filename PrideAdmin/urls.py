from django.urls import path
from .views import * 
from accounts.views import UserApi
from cars.views import SellingCarAPI
from bookings.views import ContactAPI

urlpatterns = [
    
path('user',UserApi.as_view()),
path('user/<str:pk>', UserApi.as_view()),

path('car-detail',CarAPI.as_view()),
path('car-detail/<str:pk>',CarAPI.as_view()),

path('brand',BrandAPI.as_view()),
path('brand/<str:pk>',BrandAPI.as_view()),

path('car-images',CarImagesAPI.as_view()),
path('car-images/<str:pk>',CarImagesAPI.as_view()),

path('review',ReviewsAPI.as_view()),
path('review/<str:pk>',ReviewsAPI.as_view()),

path('car-detail1',CarDetailsAPI.as_view()),
path('car-detail1/<str:pk>',CarDetailsAPI.as_view()),

path('enquiry',EnquiryAPI.as_view()),
path('enquiry/<str:pk>',EnquiryAPI.as_view()),

path('selling-request',SellingCarAPI.as_view()),
path('selling-request/<str:pk>',SellingCarAPI.as_view()),

path('contact',ContactAPI.as_view()),
path('contact/<str:pk>',ContactAPI.as_view()),

path('blog',AdminBlogAPI.as_view()),
path('blog/<str:pk>',AdminBlogAPI.as_view())

]