import json

from genie import uid, with_clip


class MinifyJsonCommand:
    def metadata(self, parameters):
        arg = "minify-json"
        return dict(
            uid=uid(1),
            arg=arg,
            title="Minify JSON",
            subtitle="Minify JSON from Clipboard",
        )

    @with_clip
    def process(self, input_from_clipboard):
        try:
            json_temp = json.loads(input_from_clipboard)
            return json.dumps(json_temp, separators=(",", ":"))
        except Exception as e:
            return "Error processing: {} - {}".format(input_from_clipboard, e)


minify_json_command = MinifyJsonCommand()
