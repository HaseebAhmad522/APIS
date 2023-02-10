from django.urls import path
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from .viewsets import SignupViewSet,LoginViewSet, UserViewSet, CategoryViewSet, BrandViewSet, CountryViewSet, StateViewSet, CityViewSet, ProductViewSet


router = DefaultRouter()
router.register('signup', SignupViewSet, basename='signup')
router.register('login', LoginViewSet, basename='login')
router.register('user', UserViewSet, basename='users')
router.register('category', CategoryViewSet, basename='categories')
router.register('brand', BrandViewSet, basename='brands')
router.register('country', CountryViewSet, basename='countries')
router.register('state', StateViewSet, basename='states')
router.register('city', CityViewSet, basename='cities')
router.register('product', ProductViewSet, basename='products')


urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),

]   

urlpatterns += router.urls