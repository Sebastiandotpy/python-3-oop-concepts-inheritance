class Color:
    """
    Represents color codes for styling text.
    """

    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    REVERSE = "\033[7m"

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    BACKGROUND_BLACK = "\033[40m"
    BACKGROUND_RED = "\033[41m"
    BACKGROUND_GREEN = "\033[42m"
    BACKGROUND_YELLOW = "\033[43m"
    BACKGROUND_BLUE = "\033[44m"
    BACKGROUND_MAGENTA = "\033[45m"
    BACKGROUND_CYAN = "\033[46m"
    BACKGROUND_WHITE = "\033[47m"

    ANIMAL_TITLE = '\033[38;5;39m'  # Light Blue
    ANIMAL_SUMMARY = '\033[38;5;33m'  # Dark Blue
    ACTION_TITLE = '\033[38;5;178m'  # Sand
    ACTION = '\033[38;5;94m'  # Light Sand




def print_styled(text, *styles):
    """
    Prints the text with the specified styles.
    """
    styled_text = "".join(styles) + text + Color.RESET
    print(styled_text)
