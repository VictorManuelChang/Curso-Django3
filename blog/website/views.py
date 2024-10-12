from django.shortcuts import render

def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'Html', 'Banco de Dados']
    data = {'name' : 'Curso de Django 3', 'lista_tecnologia' : lista}
    return render(request, 'index.html', data)