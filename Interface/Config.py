def x_pos(window, width):
    return (window.winfo_screenwidth() - width) // 2


def y_pos(window, height):
    return (window.winfo_screenheight() - height) // 2


def window_geometry(window, width, height):
    return f"{width}x{height}+{x_pos(window, width)}+{y_pos(window, height)}"


MWW = MAIN_WINDOW_WIGTH = 500
MWH = MAIN_WINDOW_HEIGHT = 260

AWW = MAIN_WINDOW_WIGTH = 350
AWH = MAIN_WINDOW_HEIGHT = 120

SWW = MAIN_WINDOW_WIGTH = 250
SWH = MAIN_WINDOW_HEIGHT = 80

SWWW = MAIN_WINDOW_WIGTH = 250
SWWH = MAIN_WINDOW_HEIGHT = 120
