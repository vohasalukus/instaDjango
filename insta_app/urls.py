from django.urls import path
from .views import category_list, filter_category, filter_author, exit, add_category, add_post, add_comm

urlpatterns = [
    path('', category_list, name='main_page'),
    path('category/<slug:slug>', filter_category, name='post_by_category'),
    path('authors/<slug:slug>', filter_author, name='post_by_author'),
    path('logout/', exit, name='exit'),
    path('add_category/', add_category, name='add_category'),
    path('add_post/', add_post, name='add_post'),
    path('add_comment/', add_comm, name='add_comment'),
]
