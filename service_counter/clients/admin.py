from django.contrib import admin

from clients.models import Client, Agreement, ClientAgent

admin.site.register(Client, Agreement, ClientAgent)
