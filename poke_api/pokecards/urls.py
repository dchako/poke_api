from django.urls import path
from .views import CardsView, GetAndFindCardsView, CreateTypesView, CreateExpansionView

urlpatterns = [
    path('pokecard', CardsView.as_view(),name="post_cards_create"),
    path('pokecard/<int:pk>', CardsView.as_view(), name="put_delete_cards"),
    path('types', CreateTypesView.as_view(),name="post_types_create"),
    path('types/<int:pk>', CreateTypesView.as_view(), name="put_delete_types"),
    path('expansion', CreateExpansionView.as_view(),name="post_expansion_create"),
    path('expansion/<int:pk>', CreateExpansionView.as_view(),name="put_delete_expansion"),
    path('getandfindcards/', GetAndFindCardsView.as_view())
]
