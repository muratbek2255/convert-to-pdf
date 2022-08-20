from django.urls import path

from src.customer.views import CustomerView, render_pdf_view, customer_render_pdf_view


urlpatterns = [
    path('', CustomerView.as_view(), name='customer-url'),
    path('test/', render_pdf_view, name='test-url'),
    path('pdf/<pk>/', customer_render_pdf_view, name='customer-detail')
]
