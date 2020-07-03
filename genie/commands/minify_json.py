import json

import clipboard

from genie import uid


class MinifyJsonCommand:
    def metadata(self, parameters):
        arg = "minify-json"
        return dict(
            uid=uid(1),
            arg=arg,
            title="Minify JSON",
            subtitle="Minify JSON from Clipboard",
        )

    def process(self):
        input_from_clipboard = clipboard.paste()
        try:
            json_temp = json.loads(input_from_clipboard)
            return json.dumps(json_temp, separators=(",", ":"))
        except Exception as e:
            return "Error processing: {} - {}".format(input_from_clipboard, e)


minify_json_command = MinifyJsonCommand()
