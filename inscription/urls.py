from django.urls import path
from .views import InscricaoVoucherViewSet

app_name = "inscricao"

urlpatterns = [
    path('inscricao/<int:pk>/voucher', InscricaoVoucherViewSet.as_view({'get': 'retrieve'}), name='inscricao_item_voucher'),
    path('inscricao/<int:pk>/voucher/pdf', InscricaoVoucherViewSet.as_view({'get': 'pdf'}), name='inscricao_item_voucher_pdf'),
]
