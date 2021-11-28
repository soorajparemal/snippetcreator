from django.urls import path
from . import views

urlpatterns = [
    path('listall/', views.SnippetListView.as_view(), name='all_snippets'),
    path('snippetdetail/<int:pk>/', views.SnippetDetailView.as_view(), name='snippet_detail'),
    path('createsnippet/', views.CreateTextSnippetView.as_view(), name='create_snippet'),
    path('updatesnippet/<int:pk>/', views.UpdateTextSnippetView.as_view(), name='update_snippet'),
    path('listalltags/', views.TagListView.as_view(), name='all_tags'),
    path('tagdetail/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('createtag/', views.CreateTagView.as_view(), name='create_tag'),
    path('deletemultiple/', views.deleteMutiple),
]