from django.shortcuts import render, HttpResponse


def show_hello(request):
    return HttpResponse('Hello!')


def show_html(request):

    context = {
        'mainigais': 'kaut ko',
        'cits': 42
    }

    return render(request,
                  template_name='index.html',
                  context=context)


# Izveidot skatu, kas pie '/get_time' parādīs laiku un datumu
# Jāizmanto datetime modulis