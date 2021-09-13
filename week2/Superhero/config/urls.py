from django.urls import path
from hero.views import SpidermanView, DrStrangeView, IndexView, DeadpoolView

urlpatterns = [
    path('', IndexView.as_view()),
    path('Dr. Strange', DrStrangeView.as_view()),
    path('Deadpool', DeadpoolView.as_view()),
    path('Spiderman', SpidermanView.as_view()),
]