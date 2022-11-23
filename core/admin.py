from django.contrib import admin
from .models import Topic, Room, Message
from django.contrib import messages
from django.utils.translation import ngettext

admin.site.register(Topic)


@admin.register(Room)
class RoomAdminModel(admin.ModelAdmin):
    fields = ['host', 'topic', 'name', 'slug', 'status', 'description', 'participants']
    list_display = ('host', 'topic', 'name', 'created')
    search_fields = ('host', 'topic', 'name')
    list_filter = ['created', 'status']

    @admin.action(description='Mark selected rooms as published')
    def make_published(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, ngettext(
            '%d room was successfully marked as published.',
            '%d rooms were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Mark selected rooms as privated')
    def make_privated(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, ngettext(
            '%d room was successfully marked as privated.',
            '%d rooms were successfully marked as privated.',
            updated,
        ) % updated, messages.SUCCESS)

# admin.site.register(Message)
@admin.register(Message)
class MessageAdminModel(admin.ModelAdmin):
    fields = ['user', 'room', 'text', 'status']
    list_display = ['user', 'room', 'text', 'status']
    search_fields = ('user', 'room', 'name')
    list_filter = ['created', 'status']

    @admin.action(description='Mark selected messages as published')
    def make_published(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, ngettext(
            '%d message was successfully marked as published.',
            '%d messages were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Mark selected messages as privated')
    def make_privated(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, ngettext(
            '%d message was successfully marked as privated.',
            '%d messages were successfully marked as privated.',
            updated,
        ) % updated, messages.SUCCESS)
