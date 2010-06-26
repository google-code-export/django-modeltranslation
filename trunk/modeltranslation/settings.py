# -*- coding: utf-8 -*-
from warnings import warn

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


if hasattr(settings, 'MODELTRANSLATION_TRANSLATION_REGISTRY'):
    TRANSLATION_REGISTRY =\
    getattr(settings, 'MODELTRANSLATION_TRANSLATION_REGISTRY', None)
elif hasattr(settings, 'TRANSLATION_REGISTRY'):
    warn('The setting TRANSLATION_REGISTRY is deprecated, use '
         'MODELTRANSLATION_TRANSLATION_REGISTRY instead.', DeprecationWarning)
    TRANSLATION_REGISTRY = getattr(settings, 'TRANSLATION_REGISTRY', None)
else:
    raise ImproperlyConfigured("You haven't set the "
                               "MODELTRANSLATION_TRANSLATION_REGISTRY "
                               "setting yet.")

DEFAULT_LANGUAGE = getattr(settings, 'MODELTRANSLATION_DEFAULT_LANGUAGE', None)

# Only override this setting if you know what you are doing!
# It merely exist for unit testing.
STD_TRANSLATION_FIELDS =\
getattr(settings, 'MODELTRANSLATION_STD_TRANSLATION_FIELDS',
        #('CharField', 'TextField', 'URLField', 'EmailField', 'XMLField',))
        ('CharField', 'TextField', 'URLField', 'EmailField', 'XMLField',
         'BooleanField', 'NullBooleanField',))
