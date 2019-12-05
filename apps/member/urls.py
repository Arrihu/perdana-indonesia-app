from django.urls import path
from apps.member import viewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=True)
router.register('list', viewsets.ArcherMemberViewset)

urlpatterns = [
    path('login', viewsets.LoginViewset.as_view(), name='login'),
    path('register', viewsets.RegisterViewset.as_view({'post': 'create'}), name='register'),
]

urlpatterns += router.urls
