from django.urls import path
from poste.views import about
from poste.views import (HomePostView,
                         PostDetailView,
                         PostCreateView,
                         PostUpdateView,
                         PostDeleteView
                         )

urlpatterns = [
    path('', HomePostView.as_view(), name='poste-home'),
    path('post/detail/<int:pk>/', PostDetailView.as_view(), name='detail-poste'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='update-poste'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='delete-poste'),
    path('post/new/', PostCreateView.as_view(), name='create-poste'),
    path('about/', about, name='poste-about')
]