from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def suma(request, num1, num2):
    suma = int(num1) + int(num2)

    return HttpResponse(num1 + " + " + num2  + " = " + str(suma))

def resta(request, num1, num2):
     resta = int(num1) - int(num2)

     return HttpResponse(num1 + " - " + num2  + " = " + str(resta))

def multi(request, num1, num2):
    multi = int(num1) * int(num2)

    return HttpResponse(num1 + " * " + num2  + " = " + str(multi))

def div(request, num1, num2):
    try:
        div = int(num1) / int(num2)
    except ZeroDivisionError:
        return HttpResponse("Estas intentando dividir entre 0")

    return HttpResponse(num1 + " / " + num2  + " = " + str(div))

def error(request):
return HttpResponse('404 Not Found')