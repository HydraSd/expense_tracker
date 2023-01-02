from django.urls import path
from . import views

urlpatterns = [
    path('expenses/', views.getExpenses),
    path('expenses/create/', views.addExpense),
    path('expenses/<int:pk>', views.getExpense),
    path('expenses/update/<int:pk>', views.upadeteExpense),
    path('expenses/delete/<int:pk>', views.deleteExpense)
]