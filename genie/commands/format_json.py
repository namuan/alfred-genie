import json

import clipboard

from genie import uid


class FormatJsonCommand:
    def metadata(self, parameters):
        arg = "format-json"
        return dict(
            uid=uid(0),
            arg=arg,
            title="Format JSON",
            subtitle="Format JSON from Clipboard",
        )

    def process(self):
        input_from_clipboard = clipboard.paste()
        try:
            json_temp = json.loads(input_from_clipboard)
            return json.dumps(json_temp, indent=4)
        except Exception as e:
            return "Error processing: {} - {}".format(input_from_clipboard, e)


format_json_command = FormatJsonCommand()
