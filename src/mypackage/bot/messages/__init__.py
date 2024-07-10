class Messages:
    welcome = "Welcome message"
    help = "Help message"
    anti_flood = "Anti flood message"
    unknown_update = "This feature is not supported yet"

    @staticmethod
    def get_message(key):
        return getattr(Messages, key, "Unknown message")

    # TODO: add messages or texts here
