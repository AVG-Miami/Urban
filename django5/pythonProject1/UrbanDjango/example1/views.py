from django.shortcuts import render
from  django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import  ContactForm

# Create your views here.
def index(request):
    title = 'мой сайт  ddd'
    text = 'my text'
    name = 'Tom'
#    list=['aa','bb','cc']
    list=[1.1,2.2,3.3]
    len_list = len (list)
    context = {
        'title': title,
        'text': text,
        'name': name,
        'list': list,
        'len_list': len_list
    }
    return  render(request,'index.html', context)

def base(request):
    return  render(request,'index2.html')


def index_x(request):
    name = request.GET.get('name', 'Guest')
    age = request.GET.get('age', 30)

    return HttpResponse (f"Hello, {name} , {age} !")


def index_y(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        print(message)
        return HttpResponse(f"You said: {message}")
    print('nook')
    return render(request, 'index3.html')

def index4(requset):

    if requset.method == 'POST':
        name = requset.POST.get('name')
        email = requset.POST.get('email')
        message = requset.POST.get('message')
        subscribe = requset.POST.get('subscribe') == 'on'

        print(f"Name : {name}")
        print(f"Email : {email}")
        print(f"Message : {message}")
        print(f"Subscribe : {subscribe}")

        return HttpResponse("Форма успешна отправлена")
    return render(requset,'index4.html')



def index5(requset):
    if requset.method == 'POST':
        form = ContactForm(requset.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subscribe = form.cleaned_data['subscribe']
            print(f"Name : {name}")
            print(f"Email : {email}")
            print(f"Message : {message}")
            print(f"Subscribe : {subscribe}")
    else:
        form = ContactForm()
        print('no')
    return render(requset,'index4.html', {'form': form})

# class index2(TemplateView):
#     template_name = 'index2.html'
