from django.urls import path
from .import views
from .views import userLogin,signup,ProductList,userLogout

urlpatterns=[
    path('home/',views.home,name='HOME'),
    path('productlist/',ProductList.as_view(),name='prolist'),
    path('profile/',views.profile_view,name='profile'),
    path('addcart/<int:product_id>/',views.add_to_cart,name='add_cart'),
    path('done<path:total_price>/',views.order_success,name='success'),
    path('order/',views.order_view,name='or_der'),
    path('cartdel<int:cart_item_id>/',views.cart_delete,name='cart_del'),
    path('login/',userLogin,name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',userLogout,name='logout'),
    
]
