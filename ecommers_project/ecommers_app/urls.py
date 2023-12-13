from . import views
from django.urls import path, include
app_name='ecommers_app'
urlpatterns = [

    # path('',views.index,name='index')
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),

]