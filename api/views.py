from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Expenses
from .serializers import ExpenseSerializer


@api_view(["GET"])
def getExpenses(request):
    expenses = Expenses.objects.all()
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def addExpense(request):
    data = request.data
    expense = Expenses.objects.create(title=data['title'], description=data['description'], catagory = data['catagory'], amount = data['amount'])
    serializer = ExpenseSerializer(expense, many=False)
    return Response(serializer.data)

@api_view(["GET"])
def getExpense(request, pk):
    expense = Expenses.objects.get(id=pk)
    serializer = ExpenseSerializer(expense, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def upadeteExpense(request,pk):
    data = request.data
    expense = Expenses.objects.get(id=pk)
    serializer = ExpenseSerializer(expense, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteExpense(request,pk):
    expense = Expenses.objects.get(id=pk)
    expense.delete()
    return Response("Expense deleted")
