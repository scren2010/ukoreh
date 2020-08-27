""" Авторизация через социальные сети """
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}

""" Подтверждени по email """
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_EMAIL_REQUIRED = True

"""С эти настройками подстверждение по email не требуеться """



ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_EMAIL_REQUIRED = False


"""Настройки отправки письма через gmail"""
"""Логин, пороль для почты"""
"""Отправка письма на почту"""

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True`
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''


"""Отправка письма в консоль"""
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# ACCOUNT_USERNAME_REQUIRED = False