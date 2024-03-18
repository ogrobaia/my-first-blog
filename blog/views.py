from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(resquest, 'blog/post_list.html', {})