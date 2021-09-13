from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class DrStrangeView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Dr. Strange',
            'body': 'My name is Stephen Strange',
            'image': '/static/images/strange.jpg'
        }


class DeadpoolView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Deadpool',
            'body': 'My name is Wade Wilson',
            'image': '/static/images/deadpool.jpg'
        }


class SpidermanView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Spiderman',
            'body': 'My name is Peter Parker',
            'image': '/static/images/spiderman.jpg'
        }