from django.urls import path
from .views import CardsView, GetAndFindCardsView, CreateTypesView, CreateExpansionView

urlpatterns = [
    path('pokecard/<int:pk>', CardsView.as_view()),
    path('Types/<int:pk>', CreateTypesView.as_view()),
    path('Expansion/<int:pk>', CreateExpansionView.as_view()),
    path('GetAndFindCards/', GetAndFindCardsView.as_view())
]
