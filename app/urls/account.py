from django.urls import path, include
from app.apis import AccountCreateView, AccountUpdateView, AccountListAV
urlpatterns = [
    path('account-create/', AccountCreateView.as_view(), name='create-account'),
    path('<uuid:pk>/account/', AccountUpdateView.as_view(), name='update-account'),
    path('account-list/', AccountListAV.as_view(), name='accountlist')
    ]