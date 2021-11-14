import clipboard


def uid(index):
    return "u-com.github.namuan-{}".format(index)


def with_clip(func):
    def wrapper(self):
        input_from_clipboard = clipboard.paste()
        return func(self, input_from_clipboard)

    return wrapper
