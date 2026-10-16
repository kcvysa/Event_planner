from django.shortcuts import render, redirect

from .forms import EventForm, SettingsForm
from .data import EVENTS
from .translations import get_translations


def _common_context(request):
    """Общий контекст для всех страниц: тема, язык, переводы."""
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'ru')
    return {
        'theme': theme,
        'language': language,
        't': get_translations(language),
    }


def index(request):
    form = EventForm()
    events = list(EVENTS)

    context = _common_context(request)
    context['form'] = form
    context['events'] = events
    context['last_visit'] = request.COOKIES.get('last_visit', None)

    response = render(request, 'events/index.html', context)
    response.set_cookie('last_visit', 'home', max_age=3600 * 24 * 30)
    return response


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            context = _common_context(request)
            context['data'] = form.cleaned_data
            return render(request, 'events/success.html', context)
    else:
        form = EventForm()

    context = _common_context(request)
    context['form'] = form
    context['events'] = EVENTS
    return render(request, 'events/index.html', context)


def settings_view(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            response = redirect('events:index')
            response.set_cookie('theme', form.cleaned_data['theme'], max_age=3600 * 24 * 30)
            response.set_cookie('language', form.cleaned_data['language'], max_age=3600 * 24 * 30)
            response.set_cookie('notification_email', form.cleaned_data['notification_email'], max_age=3600 * 24 * 30)
            response.set_cookie('notify_before', form.cleaned_data['notify_before'], max_age=3600 * 24 * 30)
            return response
    else:
        initial = {
            'theme': request.COOKIES.get('theme', 'light'),
            'language': request.COOKIES.get('language', 'ru'),
            'notification_email': request.COOKIES.get('notification_email', ''),
            'notify_before': request.COOKIES.get('notify_before', '30'),
        }
        form = SettingsForm(initial=initial)

    context = _common_context(request)
    context['form'] = form
    return render(request, 'events/settings.html', context)


def about(request):
    context = _common_context(request)
    response = render(request, 'events/about.html', context)
    response.set_cookie('last_visit', 'about', max_age=3600 * 24 * 30)
    return response