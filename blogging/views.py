from django.shortcuts import render
from blogging.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post


# def detail_view(request, poll_id):
#     try:
#         poll = User.objects.get(pk=poll_id)
#     except User.DoesNotExist:
#         raise Http404

#     if request.method == "POST":
#         if request.POST.get("vote") == "Yes":
#             poll.score += 1
#         else:
#             poll.score -= 1
#         poll.save()

#     context = {'poll': poll}
#     return render(request, 'blogging/detail.html', context)

# def stub_view(request, *args, **kwargs):
#     body = "Stub View\n\n"
#     if args:
#         body += "Args:\n"
#         body += "\n".join(["\t%s" % a for a in args])
#     if kwargs:
#         body += "Kwargs:\n"
#         body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
#     return HttpResponse(body, content_type="text/plain")


# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     template = loader.get_template('blogging/list.html')
#     context = {'posts': posts}
#     body = template.render(context)
#     return HttpResponse(body, content_type="text/html")

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'list.html', context)