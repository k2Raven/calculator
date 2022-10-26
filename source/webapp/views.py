from django.shortcuts import render


def calculate_view(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":

        try:
            first_number = int(request.POST.get('first_number'))
            second_number = int(request.POST.get('second_number'))
            action = request.POST.get('action')
            result = f"Result: {first_number} "

            if action == 'add':
                answer = first_number + second_number
                result += '+'
            elif action == 'subtract':
                answer = first_number - second_number
                result += '-'
            elif action == 'multiply':
                answer = first_number * second_number
                result += '*'
            else:
                answer = first_number / second_number
                result += '/'

            result += f" {second_number} = {answer}"

        except ValueError:
            result = "Error: enter numbers"

        except ZeroDivisionError:
            result = "Error: can't divide by zero"

        context = {
            'result': result
        }
        return render(request, 'index.html', context)
