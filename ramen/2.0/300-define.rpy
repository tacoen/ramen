init -302 python:

    RAMEN_GAME_URI = "tacoen.itch.io"
    RAMEN_IMG_EXT = ['.webp', '.png', '.jpg']
    RAMEN_IMG_SND = ['.ogg', '.mp3', '.wav']
    RAMEN_INTMIN = 0
    RAMEN_INTMAX = 100
    
    RAMEN_DEV = True
    
    if persistent.ramen is None:
        persistent.ramen={}
        
    ramen_pe = persistent.ramen
    ramen_mp = MultiPersistent(RAMEN_GAME_URI)
