import unittest
from unittest.mock import patch, mock_open
from render import Page


class TestPage(unittest.TestCase):

    def test__get_base_html_on_init(self):
        with patch("builtins.open", mock_open()) as template_reader:
            Page()
        template_reader.assert_called_with("templates/color_sample.html", 'r')

    def test_render_calls_temp(self):
        with patch("builtins.open", mock_open()):
            page = Page()
        with patch(
            "render.tempfile.NamedTemporaryFile"
        ) as temp, patch(
            "render.webbrowser.open"
        ) as writeHtml:
            page.render()
        temp.assert_called_with('w', delete=False, suffix='.html')

    def test_render_opens_browser(self):
        with patch("builtins.open", mock_open()):
            page = Page()
        with patch(
            "render.tempfile.NamedTemporaryFile"
        ) as temp, patch(
            "render.webbrowser.open"
        ) as browser:
            page.render()
        browser.assert_called_once()

    @unittest.skip('Not implemented yet.')
    def test_apply_palette(self):
        Page().apply_palette()
        self.assertTrue(False)
