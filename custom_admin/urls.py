from django.urls import path
from . import views
from custom_admin.views import admin_login_view

app_name = 'custom_admin'

urlpatterns = [
    path('adminhome/', views.admin_panel, name='admin_home'),
    path('adminlogin/', admin_login_view, name='admin_login'),
    path('adduser/', views.add_user, name='add_users'),
    path('add-product/', views.add_product, name='add_product'),
    path('view-users/', views.view_users, name='view_users'),
    path('productview/',views.product_list_view,name='prodlist'),
    path('edit-product-quantity/<int:product_id>/', views.edit_product_quantity, name='edit_product_quantity'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),


]
