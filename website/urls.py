from django.conf.urls import url
from website import views

app_name = 'website'
urlpatterns = [
    url('', views.index_view),
]