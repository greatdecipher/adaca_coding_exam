# 3.2. Optimize the following view function for better performance:
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import BlogPost
from .forms import CreateNewPost

def get_latest_posts(request):
    movie_title_list = []
    posts = BlogPost.objects.all().order_by('-publish_date')[:10]
    for i in posts:
        movie_title_list.append(i)
    # TODO: Optimize the above line for better performance.
    return render(request, 'blogpost/latest_post.html', {'posts':movie_title_list})


def create_post(request):
    if request.method == "POST":
        form = CreateNewPost(request.POST)
        if form.is_valid():
            title_save = form.cleaned_data["title"]
            content_save = form.cleaned_data["content"]
            t = BlogPost(title=title_save, content=content_save)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewPost()
    form = CreateNewPost()
    return render(request, 'blogpost/create.html', {'form':form})
