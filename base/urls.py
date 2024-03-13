from django.urls import path
from .import views

urlpatterns=[
    path('',views.endpoints),
    #path('advocates/',views.advocate_list,name="advocates"),
    # path('advocates/<str:username>/',views.advocate_details),
    
    #class base view URL
    path('advocates/',views.AdvocateList.as_view(),name="advocates"),
    path('advocates/<str:username>/',views.AdvocateDetails.as_view()),
]