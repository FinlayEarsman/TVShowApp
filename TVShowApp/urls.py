from django.urls import path
from TVShowApp import views

app_name = 'TVShowApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.tv_show, name='tv_show'),
    path('genres/', views.genres, name='genres'),
    path('genres/add', views.add_genres, name='add_genres'),
    path('genres/delete/<int:id>', views.delete_genres, name='delete_genres'),
    path('add-rating/', views.new_rating, name='new_rating'),
    path('request-show/', views.request_show, name='request_show'),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user-profile/', views.user_profile, name='user_profile'),
    path('signup/', views.sign_up, name='sign_up'),
    path('results/', views.search_results, name='search_results'),
    path('review-requests/', views.review_requests, name='review_requests'),
]
