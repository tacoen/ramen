##
#  @file icoram.rpy
#  @brief Provide Webfont icons like CSS3. Icoram is generated using Icomoon apps, https://icomoon.io/app/. Designer: Cole Bemis, License: MIT
#
#
init -198:

    python:

        try: ICO_PATH
        except NameError: ICO_PATH = ramu.fn_getdir()

        FONT_ICO_RAMEN = ICO_PATH+"/fonts/icoram.ttf"

    style icoram:
        font FONT_ICO_RAMEN
        antialias True
        size 32

    style ram_ico is icoram
    style ram_ico_text is icoram

init -197 python:

    def ico(what):

        i = {
          'love-o':';',
          'love':':',
          'warn':'+',
          'alert-triangle':'+',
          'arrow-down':'2',
          'arrow-down-left':'1',
          'arrow-down-right':'3',
          'arrow-left':'4',
          'arrow-right':'5',
          'arrow-up':'8',
          'arrow-up-left':'6',
          'arrow-up-right':'7',
          'box':'D',
          'briefcase':'B',
          'building':'=',
          'check':'C',
          'check-square':'v',
          'chevron-down':'!',
          'chevron-left':'9',
          'chevron-right':'0',
          'chevron-up':'@',
          'chevrons-down':'$',
          'chevrons-left':'%',
          'chevrons-right':'^',
          'chevrons-up':'&',
          'close':')',
          'cloud':'f',
          'cloudy':'b',
          'drawer':'D',
          'email':'u',
          'envelope':'u',
          'exit':')',
          'github':'G',
          'globe':'O',
          'help-circle':'*',
          'home':'-',
          'home1':'_',
          'inbox':'D',
          'info':'(',
          'letter':'u',
          'lightbulb':'w',
          'location':'L',
          'log-in':']',
          'log-out':'[',
          'logout':')',
          'mail':'u',
          'map-marker':'L',
          'map-o':'M',
          'message':'u',
          'minus-square':'y',
          'mobile':'P',
          'moon':'e',
          'more-horizontal':'i',
          'more-vertical':'I',
          'phone':'P',
          'phone-call':'V',
          'pin':'L',
          'plus-square':'z',
          'python':'p',
          'quit':')',
          'shield':'j',
          'shopping-bag':'S',
          'shopping-cart':'r',
          'signout':')',
          'square':'q',
          'stack':'D',
          'sun':'c',
          'sunrise':'a',
          'tablet':'P',
          'thumbs-down':'k',
          'thumbs-up':'l',
          'toggle-left':'T',
          'toggle-right':'t',
          'user':'U',
          'wallet':'W',
          'weather':'d',
          'weather1':'g',
          'windy':'h',
          'x':'X',
          'x-square':'x',
          'close':'x',
          'disk':'/',
          'save':'`',
          'load':'~',
          'cog':'|',
          'selected':'v',
          'idle':'q',
          'radio_off':',',
          'radio_on':'.',
          'road':'Z',
       }

        return i[what]
