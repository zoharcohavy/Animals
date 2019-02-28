SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
MAX_VELOCITY = 1.0

def floor(x):
    if x < 0:
        return 0
    return int(x)

def roof_x(x):
    if x > SCREEN_WIDTH:
        return int(SCREEN_WIDTH)
    return int(x)

def roof_y(x):
    if x > SCREEN_HEIGHT:
        return int(SCREEN_HEIGHT)
    return int(x)