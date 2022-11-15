from django_tables2 import TemplateColumn
from .helper_functions import get_ampel_color
from django.template import Context, Template


class AmpelTemplateColumn(TemplateColumn):
    def render(self, record, table, value, bound_column, **kwargs):
        print(record, value)
        model = self.extra_context.get("model")
        value = get_ampel_color(model, record.pk)
        context = getattr(table, "context", Context())

        print(self.extra_context)
        return super(AmpelTemplateColumn, self).render(record, table, value, bound_column, **kwargs)        
