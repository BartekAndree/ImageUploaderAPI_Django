from django.urls import path
#from rest_framework import routers

from .views import (
    FileUploadViewSet, ImageListView, 
    ImageDetailsView, GenerateLinkListView, 
    GenerateLinkDetailView, GenerateLinkCreateView, ImageDeleteView
)

#router = routers.DefaultRouter()
#router.register(r'file-upload', FileUploadViewSet)



urlpatterns = [
    path('file-upload/', FileUploadViewSet.as_view()),
    path('file-list/', ImageListView.as_view()),
    path('file-details/<int:pk>', ImageDetailsView.as_view()),
    path('file-delete/<int:pk>', ImageDeleteView.as_view()),
    path('generate-links/', GenerateLinkListView.as_view()),
    path('generate-link-details/<int:pk>', GenerateLinkDetailView.as_view()),
    path('generate-link/', GenerateLinkCreateView.as_view())
]
