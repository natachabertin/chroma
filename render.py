import tempfile
import webbrowser


TEMPLATE_FILENAME = 'templates/color_sample.html'

class Page:
    def __init__(self):
        self.baseHtml = self._get_base_html()

    def _get_base_html(self):
        with open(TEMPLATE_FILENAME, 'r') as templateFile:
            return templateFile.read()

    def apply_palette(self):
        pass

    def render(self):
        with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as webpage:
            url = 'file://' + webpage.name
            webpage.write(self.baseHtml)
        webbrowser.open(url)
