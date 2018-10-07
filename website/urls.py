from django.conf.urls import url
from website import views

app_name = 'website'
urlpatterns = [
    url(r'^$', views.index_view),
    url(r'^blog$', views.post_list, name='post_list')
]