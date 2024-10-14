from django.shortcuts import render
from  django.views.generic import TemplateView

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

# class index2(TemplateView):
#     template_name = 'index2.html'
