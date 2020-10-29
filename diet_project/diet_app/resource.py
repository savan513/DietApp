from import_export import resources
from .models import *

class UserDataResource(resources.ModelResource):
    class Meta:
        model = UserData
