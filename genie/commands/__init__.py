from genie.commands.base64_decode import base64_decode_command
from genie.commands.base64_encode import base64_encode_command
from genie.commands.format_json import format_json_command
from genie.commands.minify_json import minify_json_command
from genie.commands.unformat import unformat_command

available_commands = [
    format_json_command,
    minify_json_command,
    base64_decode_command,
    base64_encode_command,
    unformat_command,
]
