from django.urls import path
from . import views

urlpatterns = [	
	path('wisequotes-list/', views.get_wise_quotes_list, name="wisequotes-list"),
	path('recommend-list/', views.get_recommend_list, name="recommend-list"),
	path('wisequotes-detail/<str:pk>/', views.detail_wise_quotes, name="wisequotes-detail"),
	path('wisequotes-create/', views.create_wise_quotes, name="wisequotes-create"),
	path('wisequotes-update/<str:pk>/', views.update_wise_quotes, name="wisequotes-update"),
	path('wisequotes-delete/<str:pk>/', views.delete_wise_quotes, name="wisequotes-delete"),
	path('wisequotes-recommend/<str:pk>/', views.recommend_wise_quotes, name="wisequotes-recommend"),
	
]