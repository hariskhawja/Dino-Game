from config import Config

def textDisplay(text, font, coordinates, screen, pos):
    text = font.render(text, True, Config['colors']['black'])

    if pos == "c": textRect = text.get_rect(center=coordinates)

    if pos == "l": textRect= text.get_rect(topleft=coordinates)

    screen.blit(text, textRect)