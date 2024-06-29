from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Link
from .forms import LinkForm


def get_full_url(request, link_code):
    return '{0}://{1}/{2}'.format(request.scheme, request.get_host(), link_code)


def link_creator(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            foo = form.save()
            messages.add_message(request, messages.SUCCESS, 'Your URL is {}'.format(get_full_url(request, foo.shortened_link)))
    return render(request, 'link_creator.html',
                  context={'title': 'Shorten URL',
                           'url_form': LinkForm()})


def link_redirector(request, link_code):
    url = Link.objects.filter(shortened_link=link_code).first()
    if url:
        return redirect(url.original_url)
    messages.add_message(request, messages.WARNING, 'Such link does not exist')
    return redirect('creator')


def link_list(request):
    urls = [
        {
            'short': get_full_url(request, link.shortened_link),
            'original': link.original_url
        } for link in Link.objects.all()
    ]
    return render(request, 'shortened_links.html',
                  context={'title': 'List of URLs',
                           'urls': urls})
