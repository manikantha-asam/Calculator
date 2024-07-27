from django.shortcuts import render

def calculator(request):
    result = ""
    if request.method == 'POST':
        expression = request.POST.get('expression')
        try:
            result = eval(expression)
        except Exception as e:
            result = "Error"
    return render(request, 'calculator/calculator.html', {'result': result})
