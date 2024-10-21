from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.

def index(request, post_in_page = 3):


    if request.method == 'POST':
        post_in_page = int(request.POST.get('col_news'))
    else:
        post_in_page = int(request.GET.get('post_in_page'))

#print ('get method', post_in_page)

    posts = Post.objects.all().order_by('-create_at')
    list_post = []
    for i in range(1, len(posts)):
        list_post.append(i)

    paginator = Paginator(posts, post_in_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj,'post_in_page': post_in_page,
                                          'list_post':list_post})