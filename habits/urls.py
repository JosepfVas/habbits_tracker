from django.urls import path
from habits.apps import HabitsConfig
from habits.views import (
    HabitCreateAPIView,
    HabitDestroyAPIView,
    HabitListAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    PublicHabitListAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("list/", HabitListAPIView.as_view(), name="habit_list"),
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("detail/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_retrieve"),
    path("update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit_delete"),
    path("public-list/", PublicHabitListAPIView.as_view(), name="public_list"),
]
