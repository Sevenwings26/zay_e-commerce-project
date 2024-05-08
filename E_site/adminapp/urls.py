from django.urls import path 
from . import views

urlpatterns = [
    path('signup/', views.signup, name ="signup"),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out,  name="logout"),
    path('reset_password/', views.reset_password,  name="resetp"),
    path('product-upload/', views.product_upload,  name="product_upload"),
    path('product-table/', views.product_table, name="products"),
    path('users/', views.users_view, name="all-users"),
    path('delete/<int:productId>/', views.delete_product, name="delete"),
    path('modify/<int:productId>/', views.modify_product, name="modify"),
    path('order/<int:productId>/', views.order_product, name="order_product"),
]

