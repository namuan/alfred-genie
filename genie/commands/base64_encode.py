import base64

import clipboard

from genie import uid


class Base64EncodeCommand:
    def metadata(self, parameters):
        arg = "base64-encode"
        return dict(
            uid=uid(2),
            arg=arg,
            title="Base64 Encode",
            subtitle="Encode Base64 text from Clipboard",
        )

    def process(self):
        input_from_clipboard = clipboard.paste()
        try:
            return self.encode(input_from_clipboard)
        except Exception as e:
            return "Error processing: {} - {}".format(input_from_clipboard, e)

    def encode(self, src):
        src_in_bytes = bytes(src, encoding="utf-8")
        src_in_bytes_base64 = base64.standard_b64encode(src_in_bytes)
        return src_in_bytes_base64.decode(encoding="utf-8")


base64_encode_command = Base64EncodeCommand()
