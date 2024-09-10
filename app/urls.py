from django.urls import path, include

from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),

    path('blog/posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('blog/categories/<slug:category_slug>/', views.posts_by_category, name='posts_by_category'),
    path('blog/search/', views.search, name='search'),

    
]
