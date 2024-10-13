

def get_color_rgb(rgb_value: tuple[int], alpha: float = 1.0) -> tuple[float]:
    color = [1, 1, 1, 1]
    for i, color_channel in enumerate(rgb_value):
        color[i] = color_channel / 255
    color[3] = alpha
    return tuple(color)