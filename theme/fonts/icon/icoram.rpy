##
#  @file ramen_icon.rpy
#  @brief Provide Webfont icons like CSS3. ramen_icon is generated using Icomoon apps, https://icomoon.io/app/. Designer: Cole Bemis, License: MIT
#
#

init -197 python:

    def ico(what=None):
        """ Translate Ramen Ico Webfont """
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
            'mouse-l':'o',
            'mouse-r':'s'
        }
        
        if what is None:
            return i
        else:
            return i[what]
