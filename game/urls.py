from django.urls import path

from . import views

urlpatterns = [
    path('search/<int:user_id>/', views.SearchGameAPIView.as_view()),
    path('room/<int:room_id>/answer/', views.CreateGameRoomAnswerAPIView.as_view()),
    path('room/<int:room_id>/total_answers/', views.CountTotalAnswersAPIView.as_view()),
    path('room/<int:room_id>/question/<int:question_id>/total_answers/', views.CountTotalAnswersForQuestionAPIView.as_view()),
]
