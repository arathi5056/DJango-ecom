from django.urls import path
from .views import (
    ItemDetailView,
    checkout,
    HomeView,
    add_to_cart,
    remove_from_cart,
    remove_item_from_cart,
    OrderSummaryView,
    FeedbackView,
    DiscountView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('products/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('remove-item-from-cart/<slug>/', remove_item_from_cart, name='remove-item-from-cart'),
    path('discounts/', DiscountView.as_view(), name='discount-page')
]
