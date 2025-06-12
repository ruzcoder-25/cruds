from django.urls import path

from car import views

urlpatterns = [
    path('',views.car_list,name='car-list'),
    path('create/',views.create_car,name='create-car'),
    path('detail/<int:pk>/',views.detail_car,name='detail-car'),
    path('update/<int:pk>/',views.update_car,name='update-car'),
    path('delete/<int:pk>/',views.delete_car,name='delete-car'),

]