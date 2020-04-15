from django.urls import path
from crypto.views import CryptoCurrencyViewSet


app_name = "api"

urlpatterns = [
    path(
        "crypto_analysis/",
        CryptoCurrencyViewSet.as_view({"post": "create"}),
        name="crypto-analysis-details",
    )
]
