from django.conf.urls import url
from django.urls import path
from website import views

app_name = 'website'
urlpatterns = [
    url(r'^$', views.index_view),
    url(r'^blog$', views.post_list, name='post_list'),
    path('blog/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/post/new/', views.new_post, name='new_post'),
    path('blog/post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('blog/post/<int:pk>/publish/', views.publish_post, name='publish_post'),
    path('blog/post/<int:pk>/unpublish/', views.unpublish_post, name='unpublish_post'),
    path('blog/post/<int:pk>/delete/', views.delete_post, name='delete_post'),
]