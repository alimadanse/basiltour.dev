from django.urls import path
# from .views import  fill_form
from . import views


urlpatterns = [
    path('tours/', views.TourListView.as_view(), name = 'tour_list'),
    path('tours/<int:pk>/', views.TourDetailView.as_view(), name='tour_detail'),
    path('tours/<int:pk>/register/', views.TourRegisterView.as_view(), name='tour_register'),
    path('', views.home, name='home'),
]
