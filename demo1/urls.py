from django.urls import path
from demo1 import views
urlpatterns=[
    path('insert/',views.insert,name='insert'),
    path('select/',views.select,name='select'),
    path('update/',views.update,name='update'),
    path('update_value/<sid>/',views.update_value,name='update_value'),
    path('delete/',views.delete,name='delete'),
    path('delete_value/<sid>/',views.delete_value,name='delete_value'),
]