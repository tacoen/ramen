
# a copy from 00console.rpy in renpy sdk

screen _console():
    # This screen takes as arguments:
    #
    # lines
    #    The current set of lines in the input buffer.
    # indent
    #    Indentation to apply to the new line.
    # history
    #    A list of command, result, is_error tuples.
    
    layer "console"
    zorder 1500
    modal True

    if not _console.console.can_renpy():
        frame:
            style "_console_backdrop"

    frame:
        style "_console"

        has viewport:
            style_prefix "_console"
            mousewheel True
            scrollbars "vertical"
            yinitial 1.0

        has vbox

        # Draw historical console input.

        frame style "_console_history":

            has vbox:
                xfill True

            for he in history:

                frame style "_console_history_item":
                    has vbox

                    if he.command is not None:
                        frame style "_console_command":
                            xfill True
                            text "[he.command!q]" style "_console_command_text"

                    if he.result is not None:

                        frame style "_console_result":
                            if he.is_error:
                                text "[he.result!q]" style "_console_error_text"
                            else:
                                text "[he.result!q]" style "_console_result_text"

        # Draw the current input.
        frame style "_console_input":

            has vbox

            for line in lines:
                hbox:
                    spacing 4

                    if line[:1] != " ":
                        text "> " style "_console_prompt"
                    else:
                        text "... " style "_console_prompt"

                    text "[line!q]" style "_console_input_text"

            hbox:
                spacing 4

                if default[:1] != " ":
                    text "> " style "_console_prompt"
                else:
                    text "... " style "_console_prompt"

                input default default style "_console_input_text" exclude "" copypaste True


    key "game_menu" action Jump("_console_return")
    key "console_older" action _console.console.older
    key "console_newer" action _console.console.newer

# _console style

style _console is _default:
    background "#111E"
    padding (10,10)


style _console_text is ramen_gui:
    size 18
    color "#ccc"

style _console_command_text is _console_text:
    color "#fff"

style _console_input is _console_text:
    background "#0061"

style _console_input_text is _console_text:
    color "#ddd"

style _console_error_text is _console_text:
    color "#E66"
