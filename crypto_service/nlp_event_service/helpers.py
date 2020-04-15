from emot.emo_unicode import UNICODE_EMO

__author__ = "Mihail Butnaru"
__copyright__ = "Copyright 2020, All rights reserved."


def convert_emojis(text: str) -> str:
    for emot in UNICODE_EMO:
        text = text.replace(
            emot, "_".join(UNICODE_EMO[emot].replace(",", "").replace(":", "").split())
        )
    return text
