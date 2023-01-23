from food import views
from django.urls import path


app_name='food'
urlpatterns=[
    path("",views.index,name='index'),
    path('item.',views.index,name='item'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('add/',views.CreateItem.as_view(),name='create_item'),
    path('update/<int:pk>',views.update_item,name='update_item'),
    path('delete/<int:pk>', views.delete_item, name='delete_item')


]