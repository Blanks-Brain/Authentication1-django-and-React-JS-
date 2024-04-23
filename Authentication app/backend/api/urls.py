from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.CreateListNoteAPIView.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDeleteAPIView.as_view(), name="delete-note"),
]