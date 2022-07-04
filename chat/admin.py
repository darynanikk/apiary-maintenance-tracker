from django.contrib import admin

from chat.models import Room, Message


class RoomAdmin(admin.ModelAdmin):

    def get_changeform_initial_data(self, request):
        get_data = super(RoomAdmin, self).get_changeform_initial_data(request)
        get_data['host'] = request.user.pk
        return get_data


admin.site.register(Room, RoomAdmin)
admin.site.register(Message)
