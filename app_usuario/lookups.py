from selectable.base import ModelLookup
from selectable.registry import registry

from models import *

class MedicoLookup(ModelLookup):
    model = Medico
    search_fields = ('codigo__icontains', 
                     'first_name__icontains', 
                     'last_name__icontains',)
    
    def get_item_value(self, item):
        # Display for currently selected item
        return item.codigo

    def get_item_label(self, item):
        # Display for choice listings
        return u"%s" % item.first_name

registry.register(MedicoLookup)