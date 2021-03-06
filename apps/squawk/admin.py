from django.contrib import admin
from reversion.admin import VersionAdmin
from squawk.models import Contact
from squawk.models import ContactGroup
from squawk.models import ContactEndPoint
from squawk.models import APIUser
from squawk.models import Event
from squawk.models import TransmissionLog

class ContactEndPointInline(admin.TabularInline):
    model = ContactEndPoint
    extra = 1

class ContactAdmin(VersionAdmin):
    prepopulated_fields = {'slug': ("name",)}
    list_display = ('name', 'slug', 'enabled')
    search_fields = ('name', 'slug' )
    list_filter = ('enabled',)
    inlines = [ContactEndPointInline,]

    fieldsets = (
        (None,
            {'fields':(
                ('name', 'slug', 'enabled'),
            )}
        ),
    )

class ContactGroupAdmin(VersionAdmin):
    prepopulated_fields = {'slug': ("name",)}
    list_display = ('name', 'slug', 'enabled')
    search_fields = ('name', 'slug')
    list_filter = ('enabled',)
    filter_horizontal = ['contacts',]
    fieldsets = (
        (None,
            {'fields':(
                ('name', 'slug', 'enabled'),
                'contacts',
            )}
        ),
    )

class APIUserAdmin(VersionAdmin):
    prepopulated_fields = {'slug': ("name",)}
    list_display = ('name', 'api_key', 'enabled', 'is_admin')
    fieldsets = (
        (None,
            {'fields':(
                ('name', 'slug', 'enabled', 'is_admin'),
                'api_key',
            )}
        ),
    )

class EventAdmin(VersionAdmin):
    prepopulated_fields = {'slug': ("name",)}
    list_display = ('name', 'slug', 'description', 'enabled')
    search_fields = ('name', 'slug', 'description')
    list_filter = ('enabled',)
    filter_horizontal = ['contacts','groups']
    fieldsets = (
        (None,
            {'fields':(
                ('name', 'slug', 'enabled'),
                'description',
                'message',
            )}
        ),
        ("Recipients",
            {'fields':(
                'contacts',
                'groups',
            )}
        )
    )

class TransmissionLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'notification_id', 'notification', 'target',
                    'contact', 'message', 'enqueued', 'send_ok', 'delivery_confirmed')
    search_fields = ('notification_id', 'contact__name', 'gateway_response', 'message', 'address')
    list_filter = ('enqueued', 'send_ok', 'delivery_confirmed', 'notification_type', 'notification_slug')
    readonly_fields = ("status_timestamp",)
    fieldsets = (
                 ( None,
                   { 'fields' : ( 
                                 ('notification_id', 'gateway_response'),
                                 ('api_user', 'contact', 'end_point', 'address'),
                                 ('notification_type','notification_slug'),
                                 'message',
                                 ('enqueued', 'send_ok','delivery_confirmed', 
                                  'gateway_status', 'charge', 
                                  'status_timestamp')
                                 )
                    }
                  ),
                 )

admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactGroup, ContactGroupAdmin)
admin.site.register(APIUser, APIUserAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(TransmissionLog, TransmissionLogAdmin)
