from genie import uid, with_clip


class UnformatCommand:
    def metadata(self, parameters):
        arg = "unformat"
        return dict(
            uid=uid(0),
            arg=arg,
            title="Unformat",
            subtitle="Remove any formatting from clipboard contents",
        )

    @with_clip
    def process(self, input_from_clipboard):
        try:
            return input_from_clipboard
        except Exception as e:
            return "Error processing: {} - {}".format(input_from_clipboard, e)


unformat_command = UnformatCommand()
