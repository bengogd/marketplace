from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

#Home view - index.html
def home(request):
    
    return render(request, "main/index.html")
    

#For post details
def service_detail(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-published')[:4]
    context = {"post":post, 'similar_posts':similar_posts}
    return render(request, "main/service-detail.html")