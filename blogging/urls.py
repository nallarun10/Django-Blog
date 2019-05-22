from django.urls import path
from blogging.views import list_view

urlpatterns = [
    path('', list_view, name='blog_index'),
    path('blogs/<int:blog_id>/', list_view, name="blog_detail"),
]
# from blogging.views import list_view, detail_view, stub_view


# urlpatterns = [
#     path('', stub_view, name="blog_index"),
#     path('', list_view, name="blog_index"),
#     path('blogs/<int:blog_id>/', detail_view, name="blog_detail"),
# ]

# from django.urls import path
# from blogging.views import stub_view

# urlpatterns = [
#     path('', stub_view, name="blog_index"),
#     path('', list_view, name='blog_index'),
#     path('blogs/<int:blog_id>/', stub_view, name="blog_detail"),
# ]