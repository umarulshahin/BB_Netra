from django.urls import path
from Authentication_app.views import *
from rest_framework_simplejwt.views import TokenRefreshView
from Product_app.views import *

urlpatterns = [
    path('registration/', Registration,name='registration'),
    path('login/', MyTokenobtainedPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    # order management urls
    
    path ('order_management/', Order_Management.as_view(), name='order_management'),
]
