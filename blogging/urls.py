from django.urls import path, include
from blogging.views import list_view, detail_view, add_model

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('comments/add', add_model, name="blog_comments"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
