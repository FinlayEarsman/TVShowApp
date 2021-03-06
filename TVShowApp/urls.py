from django.urls import path
from TVShowApp import views

app_name = 'TVShowApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('show/<int:show_id>/', views.tv_show, name='tv_show'),
    path('like-show/', views.LikeShowView.as_view(), name='like_show'),
    path('genres/<slug:genre_name_slug>/', views.show_genre, name='show_genre'),
    path('genres/add/', views.add_genres, name='add_genres'),
    path('genres/delete/<int:id>/', views.delete_genres, name='delete_genres'),
    path('show/<int:show_id>/add-rating/', views.new_rating, name='new_rating'),
    path('request-show/', views.request_show, name='request_show'),
    path('approve-show/', views.ApproveShowRequestView.as_view(), name='approve_show'),
    path('deny-show/', views.DenyShowRequestView.as_view(), name='deny_show'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user-profile/<slug:username>/', views.user_profile, name='user_profile'),
    path('signup/', views.sign_up, name='sign_up'),
    path('results/', views.search_results, name='search_results'),
    path('review-requests/', views.review_requests, name='review_requests'),
]
