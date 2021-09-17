from django.urls import path
from .views import CreateCardsView, GetCardsView, CreateTypesView, CreateExpansionView

urlpatterns = [
    path('createCards/', CreateCardsView.as_view()),
    path('createTypes/', CreateTypesView.as_view()),
    path('createExpansion/', CreateExpansionView.as_view()),
    path('GetCards/', GetCardsView.as_view()),
    
]
