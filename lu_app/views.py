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


def get_time(request):
    from datetime import datetime

    context = {
        'now': datetime.now(),
    }

    return render(request,
                  template_name='time.html',
                  context=context)


def enter_name(request):

    if request.method == 'POST':
        name = request.POST['name']
        return HttpResponse(name)

    return render(request,
                  template_name='form.html')


def university(request):

    if request.method == 'POST':

        name = request.POST['full_name']
        maths = int(request.POST['mat'])
        latvian = int(request.POST['lat'])
        foreign = int(request.POST['for'])

        can_apply = 'can not'
        if maths >= 40 and latvian >= 40 and foreign >= 40:
            can_apply = 'can'

        context = {
            'can_apply': can_apply,
            'name': name,
        }

        return render(request,
                      template_name='uni.html',
                      context=context)

    return render(request,
                  template_name='uni_form.html')


def add_post(request):
    from datetime import datetime

    from lu_app.forms import AddPostForm

    form = AddPostForm(request.POST or None)

    if form.is_valid():

        context = {
            'title': form.cleaned_data['title'],
            'content': form.cleaned_data['content'],
            'time': datetime.now(),
        }

        return render(request,
                      template_name='post.html',
                      context=context)

    context = {
        'form': form,
    }

    return render(request,
                  template_name='add_post.html',
                  context=context)


# izveidot jaunu skatu

# ja metode ir GET
    # parādīt formu, kurā var ievadīt
    # raksta nosaukumu un saturu

# ja metode ir POST
    # parādīt raksta nosaukumu, laiku un saturu