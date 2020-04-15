from emot.emo_unicode import UNICODE_EMO


def convert_emojis(text: str) -> str:
    for emot in UNICODE_EMO:
        text = text.replace(
            emot, "_".join(UNICODE_EMO[emot].replace(",", "").replace(":", "").split())
        )
    return text
