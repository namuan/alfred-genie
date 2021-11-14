import base64

from genie import uid, with_clip


class Base64DecodeCommand:
    def metadata(self, parameters):
        arg = "base64-decode"
        return dict(
            uid=uid(3),
            arg=arg,
            title="Base64 Decode",
            subtitle="Decode Base64 text from Clipboard",
        )

    @with_clip
    def process(self, input_from_clipboard):
        try:
            return self.decode(input_from_clipboard)
        except Exception as e:
            return "Error processing: {} - {}".format(input_from_clipboard, e)

    def decode(self, src):
        src_in_bytes_base64 = bytes(src, encoding="utf-8")
        src_in_string_bytes = base64.standard_b64decode(src_in_bytes_base64)
        return src_in_string_bytes.decode(encoding="utf-8")


base64_decode_command = Base64DecodeCommand()
