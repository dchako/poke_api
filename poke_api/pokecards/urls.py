from django.urls import path
from .views import CardsView, GetAndFindCardsView, CreateTypesView, CreateExpansionView

urlpatterns = [
    path('pokecard', CardsView.as_view()),
    path('pokecard/<int:pk>', CardsView.as_view()),
    path('types', CreateTypesView.as_view()),
    path('types/<int:pk>', CreateTypesView.as_view()),
    path('expansion', CreateExpansionView.as_view()),
    path('expansion/<int:pk>', CreateExpansionView.as_view()),
    path('getandfindcards/', GetAndFindCardsView.as_view())
]
