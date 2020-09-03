""" Авторизация через социальные сети """

""" Подтверждени по email """
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_EMAIL_REQUIRED = True

"""С эти настройками подстверждение по email не требуеться """

ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True

LOGIN_REDIRECT_URL = '/api/v1/profile/token'

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
