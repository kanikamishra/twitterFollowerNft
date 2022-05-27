from django.urls import path
from app import views
urlpatterns = [
    path('nft/<int:token_id>/', views.nft_view),
]
