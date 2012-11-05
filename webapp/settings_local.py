DATABASES = {
    'default': {
        'NAME': 'heliconzoo-django-boilerplate',
        'ENGINE': 'sqlserver_ado',
        'HOST': '.\SQLEXPRESS',
        'USER': 'sa',
        'PASSWORD': 'Tester12',
        'OPTIONS' : {
            'provider': 'SQLOLEDB',
            'use_mars': False,
            },
        },
}

