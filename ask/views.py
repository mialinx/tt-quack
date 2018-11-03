from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.db import connection

from ask.forms import RegForm

posts = [
    {
        'id': i, 'title': 'title' + str(i),
        'text': 'text' + str(i), 'rating': i*i
    } for i in range(100)
]


def register(request):
    if request.method == "POST":
        f = RegForm(request.POST)
        if f.is_valid():
            user = f.save()
            login(request, user)
            return redirect("/")
    else:
        f = RegForm()
    return render(request, "register.html", {'form': f})


def login_view(request):
    next_url = request.POST.get('next') or \
        request.GET.get('next') or '/'
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )
        if not user:
            return render(request, "login.html", {
                'error': 1, 'next': next_url
            })
        else:
            login(request, user)
            return redirect(next_url)
    else:
        return render(request, "login.html", {'next': next_url})


def hello(request):
    pagenum = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        page = paginator.page(pagenum)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context = {
        'user': {
            'name': request.user.username,
            'nick': request.user.is_authenticated,
        },
        'page': page,
        'paginator': paginator,
        'posts': page.object_list,
        'test': request.GET.get('test'),
    }
    return render(request, "ver1/hello.html", context)


@login_required
def secret(request):
    return render(request, "secret.html", {})


def like(request):
    if request.user.is_anonymous:
        return JsonResponse({'status': 'fail', 'error': 'no_auth'})
    # TODO:
    return JsonResponse({'status', 'ok'})
