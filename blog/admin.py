from django.contrib import admin
from .models import Table
from .models import TableImage
from .models import MyErrors


admin.site.register(Table)
admin.site.register(TableImage)
admin.site.register(MyErrors)
