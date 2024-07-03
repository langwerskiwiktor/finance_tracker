from django.urls import path
from .views import TransactionView, TransactionListView, AccountView, AccountListView, UserView, UserListView, CategoryView, CategoryListView, TransactionDetailView, UserDetailView, AccountDetailView, CategoryDetailView, UserUpdateView, UserDestroyView, TransactionUpdateView, TransactionDestroyView, AccountUpdateView, AccountDestroyView, CategoryUpdateView , CategoryDestroyView




urlpatterns = [
    path('user/', UserView.as_view()),                              #Tworzenie nowej transakcji:
    path('user_list/', UserListView.as_view()),                     #Pobieranie listy transakcji:
    path('users/<int:pk>/', UserDetailView.as_view()),              #Pobieranie szczegółów jednej transakcji
    path('users_update/<int:pk>/', UserUpdateView.as_view()),       #Aktualizowanie istniejącej transakcji
    path('users_delete/<int:pk>/', UserDestroyView.as_view()),      #Usuwanie 

    path('transaction/', TransactionView.as_view()),
    path('transaction_list/', TransactionListView.as_view()),
    path('transactions/<int:pk>/', TransactionDetailView.as_view()),
    path('transactions_update/<int:pk>/', TransactionUpdateView.as_view()),
    path('transaction_delete/<int:pk>/', TransactionDestroyView.as_view()),

    path('account/', AccountView.as_view()),
    path('account_list/', AccountListView.as_view()),
    path('accounts/<int:pk>/', AccountDetailView.as_view()),
    path('accounts_update/<int:pk>/', AccountUpdateView.as_view()),
    path('accounts_delete/<int:pk>/', AccountDestroyView.as_view()),


    path('category/', CategoryView.as_view()),
    path('category_list/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('category_update/<int:pk>/', CategoryUpdateView.as_view()),
    path('category_delete/<int:pk>/', CategoryDestroyView.as_view()),
]
