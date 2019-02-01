from django.views.generic.base import TemplateView
from django.apps import apps

# TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['app_list'] = ['books']
        dictVerbose = {} # No need to hard-code app's names
        for app in apps.get_app_configs():
            """
            apps.get_app_configs() returns a list of Configs added to INSTALLED_APPS in settings.py.
            """
            if 'site-packages' not in app.path: # if the app is not an externerl app
                """
                app.path is an actual path of each app. 'site-packages' means external library app.
                """
                dictVerbose[app.label] = app.verbose_name
                """
                verbose_name is defiend in each app's apps.py.
                (app.label = 'books', app.verbose_name = 'Book-Author-Publisher App')
                """
        context['verbose_dict'] = dictVerbose
        return context