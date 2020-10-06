from django.urls import path

from . import views

urlpatterns = [
    path('', views.WelcomeView.as_view()),
    path('home/', views.BlogHomeView.as_view(), name='home'),
    path('news-feed/', views.BlogPublicView.as_view(), name='news_feed'),
    path('news-feed/<slug:category_url>/', views.FilterPublicView.as_view(), name='public_filter'),
    path('home/<slug:category_url>/', views.FilterHomeView.as_view(), name='home_filter'),
    path('create-post/', views.CreatePostView.as_view(), name='create_post'),
    path('edit-post/<slug:slug>/', views.UpdatePostView.as_view(), name='edit_post'),
    path('delete-post/<slug:slug>/', views.DeletePostView.as_view(), name='delete_post'),
    path('<slug:slug>/', views.BlogDetailView.as_view(), name='post_detail')
]
