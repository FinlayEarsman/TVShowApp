from django.urls import path
from TVShowApp import views

app_name = 'TVShowApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('Show/', views.tv_show, name='tv_show'),
path('genres/', views.genres, name='genres'),
path('add-rating/', views.new_rating, name='new_rating'),
path('request-show/', views.request_show, name='request_show'),
path('login/', views.login, name='login'),
path('user-profile/', views.user_profile, name='user_profile'),
path('signup/', views.sign_up, name='sign_up'),
path('results/', views.search_results, name='search_results'),
path('review-requests/', views.review_requests, name='review_requests'),
]
