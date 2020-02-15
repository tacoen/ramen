##
#  @file icoram.rpy
#  @brief Provide Webfont icons like CSS3. Icoram is generated using Icomoon apps, https://icomoon.io/app/. Designer: Cole Bemis, License: MIT
#
#
init -198:

    python:

        try: ICO_PATH
        except NameError: ICO_PATH=ramu.fn_getdir()

        FONT_ICO_RAMEN=ICO_PATH+"/fonts/ramen-ico.ttf"

    style icoram:
        font FONT_ICO_RAMEN
        antialias True
        size 32

    style ram_ico is icoram
    style ram_ico_text is icoram

init -197 python:

    def ico(what=None):
        i={
            'sun1':'d',
            'sun2':'a',
            'sun3':'c',
            'sun4':'m',
            'sun5':'g',
            'sun6':'e',
            'weather1':'b',
            'weather2':'f',
            'weather3':'h',
            'radio_on':'.',
            'radio_off':',',
            'list':'>',
            'menu':'<',
            'lightbulb':'w',
            'messages':'u',
            'exit':')',
            'log-in':']',
            'log-down':'`',
            'log-up':'~',
            'log-out':'[',
            'home':'-',
            'home-o':'_',
            'building':'=',
            'road':'Z',
            'alert':'+',
            'info':'(',
            'help':'*',
            'chevrons-up':'&',
            'chevrons-right':'^',
            'chevrons-left':'%',
            'chevrons-down':'$',
            'chevron-up':'@',
            'chevron-right':'0',
            'chevron-left':'9',
            'chevron-down':'!',
            'arrow-up':'8',
            'arrow-up-right':'7',
            'arrow-up-left':'6',
            'arrow-right':'5',
            'arrow-left':'4',
            'arrow-down-right':'3',
            'arrow-down':'2',
            'arrow-down-left':'1',
            'toggle-right':'t',
            'toggle-left':'T',
            'more-horizontal':'i',
            'more-vertical':'I',
            'close':'X',
            'check':'C',
            'plus-square':'z',
            'minus-square':'y',
            'x-square':'x',
            'check-square':'v',
            'square':'q',
            'thumbs-up':'l',
            'thumbs-down':'k',
            'heart-outline':';',
            'heart':':',
            'shield':'j',
            'globe':'O',
            'user':'U',
            'phone-call':'V',
            'save':'/',
            'settings':'|',
            'shopping-bag':'S',
            'shopping-cart':'r',
            'briefcase':'B',
            'pin':'L',
            'map':'M',
            'wallet':'W',
            'stack':'D',
            'phone':'P',
            'github':'G',
            'python':'p',
        }
        
        if what is None:
            return i
        else:
            return i[what]
