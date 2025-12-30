from django.urls import path

from . import views

urlpatterns = [


    path('subscription-list/',views.SubscriptionView.as_view(),name='subscription-list'),

    path('subscription-plan-create/',views.SubscriptionPlanCreateView.as_view(), name='subscription-plan-create'),

    # path('subscription-plan-edit/<uuid:uuid>/edit/', views.SubscriptionPlanEditView.as_view(), name='subscription-plan-edit'),

    path('subscription-plan-edit/<uuid:uuid>/', views.SubscriptionPlanEditView.as_view(), name='subscription-plan-edit'),

    path('subscription-plan-delete/<uuid:uuid>/', views.SubscriptionPlanDeleteView.as_view(), name='subscription-plan-delete'),

]