from django.urls import path
from . import views


urlpatterns = [
    path("notes/", views.GetNotes),
    path("note/<int:note_id>/", views.GetNote),
    path("note/create/", views.CreateNote),
    path("note/update/<int:note_id>/", views.UpdateNote),
    path("note/delete/<int:note_id>/", views.DeleteNote),
]
