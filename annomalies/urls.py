from django.urls import path,include
from annomalies import views 

urlpatterns= [
    path('issues',views.issues.as_view(), ),
    path('parcel',views.parcel.as_view(),),
    path('parcel/<int:pk>/',views.parcel.as_view()),
    path('issue_details/<int:pk>/',views.issue_details.as_view()),
    path('issue_details',views.issue_details.as_view()),
]