from django import forms
from .data import CATEGORIES


class EventForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label='Название события',
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите название'})
    )
    date = forms.DateField(
        label='Дата',
        widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'date'})
    )
    time = forms.TimeField(
        label='Время',
        widget=forms.TimeInput(attrs={'class': 'form-input', 'type': 'time'})
    )
    category = forms.ChoiceField(
        choices=CATEGORIES,
        label='Категория',
        widget=forms.Select(attrs={'class': 'form-input'})
    )
    description = forms.CharField(
        required=False,
        label='Описание',
        widget=forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Описание события'})
    )
    notify = forms.BooleanField(
        required=False,
        initial=True,
        label='Включить уведомление'
    )


class SettingsForm(forms.Form):
    theme = forms.ChoiceField(
        choices=[('light', 'Светлая'), ('dark', 'Тёмная')],
        label='Тема оформления',
        widget=forms.Select(attrs={'class': 'form-input'})
    )
    language = forms.ChoiceField(
        choices=[('ru', 'Русский'), ('en', 'English')],
        label='Язык интерфейса',
        widget=forms.Select(attrs={'class': 'form-input'})
    )
    notification_email = forms.EmailField(
        required=False,
        label='Email для уведомлений',
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'you@example.com'})
    )
    notify_before = forms.ChoiceField(
        choices=[('5', 'За 5 минут'), ('30', 'За 30 минут'), ('60', 'За 1 час'), ('1440', 'За 1 день')],
        label='Напоминать',
        widget=forms.Select(attrs={'class': 'form-input'})
    )