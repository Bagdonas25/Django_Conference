from .views import ConferenceListView, ConferenceDetailView, ConferenceLikeView, CreateCommentView, CreateConferenceView
from django.urls import path


urlpatterns = [
    path("", ConferenceListView.as_view()),
    path("<int:pk>/", ConferenceDetailView.as_view(), name = "conference-detail"),
    path("like/<int:konferencijos_id>/",
         ConferenceLikeView.as_view(),
         name = "conference-like"),
    path("<int:pk>/comments/", CreateCommentView.as_view(), name='create-comment'),
    path("new/", CreateConferenceView.as_view(), name = 'create-conference'),
]