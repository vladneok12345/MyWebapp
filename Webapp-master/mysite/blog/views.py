from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from django.views import View
from .models import Post, PostPoint, Comment, User
from .forms import CommentForms, LoginForm, RegisterForm
from django.db.models import Count
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

from taggit.models import Tag

@login_required(login_url='blog:login')
def post_list(request, tag_slug=None):
    object_list=Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    items_per_page = 3
    paginator=Paginator(object_list, items_per_page)
    page = request.GET.get('page', 1)
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request,'blog/post/list.html',{'posts':posts})




def post_detail(request, year, month, day, post):
    post_object = get_object_or_404(Post, slug=post, status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    post_points = PostPoint.objects.filter(post=post_object)

    comments = post_object.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':

        comment_form = CommentForms(data=request.POST)
        if comment_form.is_valid():
            cd = comment_form.cleaned_data
            new_comment = Comment(post=post_object, name=cd['name'], email=cd['email'], body=cd['body'])
            new_comment.save()
    else:
        comment_form = CommentForms()

    post_tags_ids=post_object.tags.values_list('id',flat=True)
    similar_posts=Post.objects.filter(tags__in=post_tags_ids,status='published').exclude(id=post_object.id)
    similar_posts=similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:3]

    return render(request, 'blog/post/detail.html', {'post': post_object,
                                                     'post_points': post_points,
                                                     'comments': comments,
                                                     'new_comment': new_comment,
                                                     'comment_form': comment_form,
                                                     'similar_posts': similar_posts
                                                     })

@login_required(login_url='blog:login')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect!')
    context = {}
    return render(request, 'registration/login.html', context)

def logout_view(request):
    messages.success(request, 'Successfully logged out')
    logout(request)
    return redirect('login')

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'registration/register.html', context)

def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user':current_user}
        return render(request, 'blog/base.html', param)
    else:
        return redirect('login')
    return render(request, 'registration/login.html')


@login_required
def profile(request):
    return render(request, 'blog/account/dashboard.html')