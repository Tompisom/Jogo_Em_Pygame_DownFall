from pygame import *
DONE = False
screen = display.set_mode((1024,768))
alphaSurface = Surface((1024,768)) # The custom-surface of the size of the screen.
alphaSurface.fill((255,252,255)) # Fill it with whole white before the main-loop.
alphaSurface.set_alpha(0) # Set alpha to 0 before the main-loop. 
alph = 0 # The increment-variable.
while not DONE:
    screen.fill((0,0,0)) # At each main-loop fill the whole screen with black.
    alph += 1 # Increment alpha by a really small value (To make it slower, try 0.01)
    alphaSurface.set_alpha(alph) # Set the incremented alpha-value to the custom surface.
    screen.blit(alphaSurface,(0,0)) # Blit it to the screen-surface (Make them separate)

    # Trivial pygame stuff.
    if key.get_pressed()[K_ESCAPE]:
        DONE = True
    for ev in event.get():
        if ev.type == QUIT:
            DONE = True
    display.flip() # Flip the whole screen at each frame.
quit()