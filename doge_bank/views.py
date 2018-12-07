from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('accounts:index'))
        return super().dispatch(*args, **kwargs)
