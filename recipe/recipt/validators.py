from django import forms


def validate_not_empty(value):
    if value == '':
        raise forms.ValidationError(
            'А кто поле будет заполнять, Пушкин?',
            params={'value': value},
        )
    

def validate_capitalized(value):
    """
    Проверяет, начинается ли строка с заглавной буквы.

    """
    if not value[0].isupper():
        raise forms.ValidationError(
            "Строка должна начинаться с заглавной буквы."
        )


def validate_non_negative(value):
    """
    Проверяет, является ли число неотрицательным (>= 0).

    """
    if value < 0:
        raise forms.ValidationError(
            "Число не должно быть отрицательным."
        )
    

