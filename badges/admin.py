from django.contrib import admin

from badges.models import Model3d, Badge, UserBadge

admin.site.register(Model3d)
admin.site.register(Badge)
admin.site.register(UserBadge)