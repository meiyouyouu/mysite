from django.conf.urls import url
from . import views

app_name='account'
urlpatterns = [
    url(r'^login/$',views.user_login,name="user_login"),
    # url(r'(?P<article_id>\d)/$',views.blog_article,name="blog_detail"),
]