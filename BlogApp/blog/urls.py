from django.urls import path
from .views import HomeView, BlogsView, BlogDetailsView, BlogsByCategory
from . import views

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("home", HomeView.as_view(), name="home"),
    path("blogs", BlogsView.as_view(), name="blogs"),
    path('category/<slug:slug>', BlogsByCategory.as_view(), name="blogs_by_category"),  # Add .as_view()
    path("blogs/<slug:slug>", BlogDetailsView.as_view(), name="detail"),
    path('blogs/', views.BlogListCreateAPIView.as_view(), name='blog-list'),
    path('blogs/<int:pk>', views.BlogDetailAPIView.as_view(), name='blog-detail'),
    path('add_blog/', views.AddBlogView.as_view(), name='add_blog'),
]
