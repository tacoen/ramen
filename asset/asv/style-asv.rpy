style devtheme is default
style devtheme_text is ramen_gui:
    color "#ccc"

style devtheme_button is button
style devtheme_button_text_font is ramen_gui

style rai is default
style rai_text is ramen_gui:
    size 16

style rai_nav is rai

style rai_nav_button:
    background "#2349"
    hover_background "#4569"
    selected_background "#7899"
    xsize 168

style rai_nav_button_text is rai_text:
    color "#ccc"
    hover_color "#fff"
    selected_color "#fff"
    text_align 1.0
    size 18

style rai_tab is rai_nav_button:
    xsize None

style rai_tab_text is rai_nav_button_text

style rai_ctl is rai
style rai_ctl_text is rai_text:
    line_leading 8

style rai_ctl_button is button

style rai_ctl_button_text is rai_text:
    size 24
    color "#ddd"
    hover_color "#fff"

style rai_opt is rai
style rai_opt_text is rai_text:
    color "#ddd"

style rai_opt_button is button:
    selected_background "#fc3"

style rai_opt_button_text is rai_opt_text:
    hover_color "#fff"
    selected_color "#000"
