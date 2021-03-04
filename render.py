import tempfile
import webbrowser


TEMPLATE_FILENAME = 'templates/color_sample.html'

class Page:
    def __init__(self):
        self.baseHtml = self._get_base_html()

    @staticmethod
    def _get_base_html():
        with open(TEMPLATE_FILENAME, 'r') as templateFile:
            return templateFile.read()

    def apply_palette(self):
        pass

    def render(self):
        with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as webpage:
            url = 'file://' + webpage.name
            webpage.write(self.baseHtml)
        webbrowser.open(url)

class ComboTest:

    WEB_TESTER = 'https://www.colorcombos.com/combotester.html?{q}'

    def __init__(self, palette):
        self.query = self._get_query(palette)

    def show(self):
        """Show the EXTERNAL webpage with the chosen colors."""
        webbrowser.open(
            self.WEB_TESTER.format(q=self.query)
        )

    @staticmethod
    def _get_query(palette):
        """ Generate the query to request the color palette.

        Example:
        color0=445566&color1=427b90&color2=58737e&color3=b68e4b
        """
        #TODO: refact HexColors to make it suscriptable or make get hex name a public method.
        params = [
            f"color{index}={color._get_hex_name()[1:]}"
            for index, color in enumerate(palette.colors)
        ]
        return '&'.join(params)
