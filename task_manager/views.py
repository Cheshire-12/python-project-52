from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

def test_error(request):
    # This view is used to test error handling and logging.
    # It intentionally raises an exception to simulate an error scenario.
    raise Exception("This is a test exception for error handling.")