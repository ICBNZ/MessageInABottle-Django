# This is a fairly standard Django settings file, with some special additions
# that allow addon applications to auto-configure themselves. If it looks
# unfamiliar, please see our documentation:
#
#   http://docs.divio.com/en/latest/reference/configuration-settings-file.html
#
# and comments below.


# INSTALLED_ADDONS is a list of self-configuring Divio Cloud addons - see the
# Addons view in your project's dashboard. See also the addons directory in
# this project, and the INSTALLED_ADDONS section in requirements.in.

INSTALLED_ADDONS = [
    # Important: Items listed inside the next block are auto-generated.
    # Manual changes will be overwritten.

    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'django-filer',
    # </INSTALLED_ADDONS>
]

# Now we will load auto-configured settings for addons. See:
#
#   http://docs.divio.com/en/latest/reference/configuration-aldryn-config.html
#
# for information about how this works.
#
# Note that any settings you provide before the next two lines are liable to be
# overwritten, so they should be placed *after* this section.

import aldryn_addons.settings
aldryn_addons.settings.load(locals())

# Your own Django settings can be applied from here on. Key settings like
# INSTALLED_APPS, MIDDLEWARE and TEMPLATES are provided in the Aldryn Django
# addon. See:
#
#   http://docs.divio.com/en/latest/how-to/configure-settings.html
#
# for guidance on managing these settings.
AUTH_USER_MODEL = 'accounts.User'

INSTALLED_APPS.extend([
   'accounts',
   'blog',
   'about',
   'mathfilters',
   'social_django',
    'jquery',
    'bootstrap4',
    'bootstrap_datepicker_plus',
    'rest_framework',
    'django_social_share',
    # Extend the INSTALLED_APPS setting by listing additional applications here
])
MIDDLEWARE.extend([
    'social_django.middleware.SocialAuthExceptionMiddleware',     # Social Auth
])

# Social Auth
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    #'repairs_accounts.pipeline.get_username',
    'social_core.pipeline.mail.mail_validation',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details'
)
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_USER_FIELDS = ['username', 'first_name', 'last_name', 'email']

BOOTSTRAP4 = {
    'include_jquery': True,
}
TEMPLATES[0]["OPTIONS"]["context_processors"].append(
'django.template.context_processors.debug'),
TEMPLATES[0]["OPTIONS"]["context_processors"].append(
'django.template.context_processors.request'),
TEMPLATES[0]["OPTIONS"]["context_processors"].append(
'django.contrib.auth.context_processors.auth'),
TEMPLATES[0]["OPTIONS"]["context_processors"].append(
'django.contrib.messages.context_processors.messages'),
TEMPLATES[0]["OPTIONS"]["context_processors"].append(
'social_django.context_processors.backends'),
TEMPLATES[0]["OPTIONS"]["context_processors"].append(        # Social Auth
'social_django.context_processors.login_redirect'),  # Social Auth)
TEMPLATES[0]["OPTIONS"]["context_processors"].append(
'django.template.context_processors.media'),

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

FILER_ENABLE_PERMISSIONS = True
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
# Social Auth
SOCIAL_AUTH_FACEBOOK_KEY = 'XXXXXXXX'        # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'XXXXXXXX' # App Secret


# Additional locations of static files
#STATICFILES_DIRS = '/home/static',

MEDIA_ROOT = '/data/media/'

MEDIA_URL = '/media/'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

#password reset section/'stuff'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'messageinabottlenewzealand@gmail.com'
EMAIL_HOST_PASSWORD = 'XXXXXXXX'
SERVER_EMAIL = 'messageinabottlenewzealand@gmail.com'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# To see the settings that have been applied, use the Django diffsettings
# management command.
# See https://docs.divio.com/en/latest/how-to/configure-settings.html#list
