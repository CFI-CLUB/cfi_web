from club import views
from django.urls import path

app_name = 'club'

urlpatterns = [
    path('', views.index, name='index'),
    path('goto/', views.goto_url, name="goto"),
    path('ideas/', views.blog_list, name="blog_list"),
    path('<slug:title_slug>/', views.blog, name="blog"),
]

# depreciated code
# path('submit-ideas/', views.submit_ideas, name="submit_ideas"),


