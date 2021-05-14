from django.shortcuts import render

# Create your views here.
from instagram.models import Post


def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    return render(request, 'instagram/post_list.html', {'post_list': qs, 'q': q})


def post_detail(request, pk):
    pass
