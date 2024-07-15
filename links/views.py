from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from ipware.ip import get_client_ip
from .models import Link, Click
from .forms import LinkForm


def get_full_url(request, link_code=''):
    return f'{request.scheme}://{request.get_host()}/{link_code}'


def link_creator(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'New URL created')
    
    links = Link.objects.all().order_by('-id')
    paginator = Paginator(links, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'link_creator.html',
                  context={
                        'title': 'Shorten URL',
                        'url_form': LinkForm(),
                        'urls': page_obj,
                        'site_url': request.get_host()
                    })


def link_redirector(request, link_code):
    url = Link.objects.filter(shortened_link=link_code).first()
    print(get_client_ip(request))
    if url:
        Click.objects.create(
            link=url,
            source_ip=get_client_ip(request)[0]
        )
        return redirect(url.original_url)
    messages.add_message(request, messages.WARNING, 'Such link does not exist')
    return redirect('creator')

