import re


def copy_paste(string):
    def substring_finder(substring, string):
        return [x.start() for x in re.finditer(re.escape(substring), string)]

    ctrl_v_ids = substring_finder("[CTRL+V]", string)
    id_adjust = 0
    clipboard = ""

    for ctrl_v in sorted(ctrl_v_ids):
        # Find actions before ctrl v
        possible_ctrl_c = [
            x + id_adjust
            for x in substring_finder("[CTRL+C]", string)
            if x + id_adjust < ctrl_v
        ]
        possible_ctrl_x = [
            x + id_adjust
            for x in substring_finder("[CTRL+X]", string)
            if x + id_adjust < ctrl_v
        ]

        possible_actions = possible_ctrl_c + possible_ctrl_x

        if possible_actions:
            for action in sorted(possible_actions):
                clipboard = string[: action - id_adjust]

                # Cut and paste
                if action in possible_ctrl_x:
                    # Remove specific [CTRL+X] and preceding text
                    string = string[action + 8 - id_adjust :]
                    # Adjust for new string length
                    id_adjust += action + 8 - id_adjust

                # Copy and paste
                else:
                    # Remove specific [CTRL+C]
                    string = (
                        string[: action - id_adjust] + string[action + 8 - id_adjust :]
                    )
                    # Adjust for new string length
                    id_adjust += 8

        # Remove specific [CTRL+V], paste and adjust
        string = (
            string[: ctrl_v - id_adjust] + clipboard + string[ctrl_v + 8 - id_adjust :]
        )
        id_adjust += 8 - len(clipboard)

    print(string)

    return string


if __name__ == "__main__":

    copy_paste("the big red[CTRL+C] fox jumps over [CTRL+V] lazy dog.")
    copy_paste("[CTRL+V]the tall oak tree towers over the lush green meadow.")
    copy_paste("the sun shines down[CTRL+C] on [CTRL+V][CTRL+C] the busy [CTRL+V].")
    copy_paste("[CTRL+V]the tall oak tree towers over the lush green meadow.")
    copy_paste("a majestic lion[CTRL+C] searches for [CTRL+V] in the tall grass.")
    copy_paste(
        "the shimmering star[CTRL+X]Twinkling in the dark, [CTRL+V] shines bright."
    )
    copy_paste(
        "[CTRL+X]a fluffy white cloud drifts [CTRL+V][CTRL+C] across the sky, [CTRL+V]"
    )
