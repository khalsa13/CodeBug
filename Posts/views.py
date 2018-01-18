from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from urllib.parse import quote_plus
from .forms import PostForm
from .models import Post
from django.contrib.contenttypes.models import ContentType
from Comments.models import Comment
# Create your views here.


def create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post added in feed")

    context = {
        "form": form,
    }
    return render(request, "form_add.html", context)


def feed_home(request):
    query_set_list=Post.objects.all()
    requestReceive = request.GET.get("q")
    if requestReceive:
        query_set_list = query_set_list.filter(title__icontains=requestReceive)

    paginator = Paginator(query_set_list, 24)  # Show 25 contacts per page


    page = request.GET.get('page')
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query_set = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query_set = paginator.page(paginator.num_pages)

    context={
        "query_set":query_set,
    }
    return render(request,"feeds.html",context)

def details(request,slug=None):
    instance=get_object_or_404(Post,slug=slug)
    cont_type=ContentType.objects.get_for_model(Post)
    obj_id=instance.id
    comm=Comment.objects.filter(content_type=cont_type, object_id=obj_id)
    share_url = quote_plus(instance.content)
    context = {
        "instance": instance,
        "share_url":share_url,
        "comments":comm,
    }
    return render(request, "FeedDetails.html", context)

