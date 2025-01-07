from django.contrib import admin
from .models import *

admin.site.register(Organization)
admin.site.register(TeamMember)
admin.site.register(Activity)
admin.site.register(Issue)
admin.site.register(HelpOption)
admin.site.register(Resource)
admin.site.register(Donation)

