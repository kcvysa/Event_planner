from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EventForm, SettingsForm
from .data import EVENTS


def index(request):
    """Главная страница со списком событий и формой добавления."""
    form = EventForm()
    events = list(EVENTS)

    # Читаем настройки из cookies
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'ru')
    last_visit = request.COOKIES.get('last_visit', None)

    # Сохраняем последнюю посещённую страницу
    response = render(request, 'events/index.html', {
        'form': form,
        'events': events,
        'theme': theme,
        'language': language,
        'last_visit': last_visit,
    })
    response.set_cookie('last_visit', 'Главная', max_age=3600 * 24 * 30)
    return response


def add_event(request):
    """Обработка формы добавления события."""
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            # Просто показываем успех (данные не сохраняем в БД)
            data = form.cleaned_data
            return render(request, 'events/success.html', {'data': data})
    else:
        form = EventForm()
    return render(request, 'events/index.html', {'form': form, 'events': EVENTS})


def settings_view(request):
    """Страница настроек с сохранением в cookies."""
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            response = redirect('events:index')
            # Сохраняем все настройки в cookies (30 дней)
            response.set_cookie('theme', form.cleaned_data['theme'], max_age=3600 * 24 * 30)
            response.set_cookie('language', form.cleaned_data['language'], max_age=3600 * 24 * 30)
            response.set_cookie('notification_email', form.cleaned_data['notification_email'], max_age=3600 * 24 * 30)
            response.set_cookie('notify_before', form.cleaned_data['notify_before'], max_age=3600 * 24 * 30)
            return response
    else:
        # Заполняем форму значениями из cookies
        initial = {
            'theme': request.COOKIES.get('theme', 'light'),
            'language': request.COOKIES.get('language', 'ru'),
            'notification_email': request.COOKIES.get('notification_email', ''),
            'notify_before': request.COOKIES.get('notify_before', '30'),
        }
        form = SettingsForm(initial=initial)

    return render(request, 'events/settings.html', {
        'form': form,
        'theme': request.COOKIES.get('theme', 'light'),
    })


def about(request):
    response = render(request, 'events/about.html')
    response.set_cookie('last_visit', 'О проекте', max_age=3600 * 24 * 30)
    return response