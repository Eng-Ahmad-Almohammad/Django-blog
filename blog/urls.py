from django.urls import path


from .views import( PostListView, 
                    PostDetailView, 
                    category, 
                    search, 
                    PostCreateView, 
                    UserPosts
                    )


urlpatterns = [

    path('search/', search, name="search"),
    path('create/', PostCreateView.as_view() ,name='post_create'),
    path('my-posts/', UserPosts.as_view() ,name='my_posts'),
    path('', PostListView.as_view(), name='frontpage'),
    path('<slug:category_slug>/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/', category, name='category'),
]