from django.http import HttpResponse

def index(request):
    return HttpResponse("sumar/a/b , restar/a/b, multiplicar/a/b")

def sumar(request, num1, num2):
    sumar = num1 + num2
    return HttpResponse("La suma de {}+{}={}".format(num1,num2,sumar))

def restar(request, num1, num2):
    restar = num1 - num2
    return HttpResponse("La resta de {}-{}={}".format(num1,num2,restar))

def multiplicar(request, num1, num2):
    multiplicar = num1 * num2
    return HttpResponse("La multiplicacion de {}*{}={}".format(num1,num2,multiplicar))
