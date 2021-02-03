from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from notes import views

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('notes/', views.NoteList.as_view(),name='note-list'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(),name='note-detail'),
    path('users/', views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(),name='user-detail'),
    path('share/<int:note_id>/<int:viewer_id>/',views.shared_notes,name='note-share'),
])
