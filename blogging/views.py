from django.shortcuts import render

from django.shortcuts import render
from django.http import Http404
from blogging.models import User

def list_view(request):
    context = {'users': User.objects.all()}
    return render(request, 'blogging/list.html', context)

def detail_view(request, poll_id):
    try:
        poll = User.objects.get(pk=poll_id)
    except User.DoesNotExist:
        raise Http404

    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

    context = {'poll': poll}
    return render(request, 'blogging/detail.html', context)
