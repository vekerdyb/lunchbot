# Map of true/false (ie. yes/no) responses to appropriate Slack emoji names.
import random

emojis = {
    True: [
        "thumbsup",
        "heart_eyes",
        "heart_eyes_cat",
        "grinning_face_with_star_eyes",
        "ok_hand",
        "muscle",
        "100",
        "sunglasses",
        "money_mouth_face",
        "chart",
        "moneybag",
        "kissing_heart",
        "angel",
        "dancer",
        "man_dancing",
        "the_horns",
        "call_me_hand",
        "fist",
        "i_love_you_hand_sign",
        "raised_hands",
        "handshake",
        "clap",
        "heart",
        "tada",
        "sparkles",
        "medal",
        "star",
        "rainbow",
        "fire",
        "white_check_mark",
        "heavy_check_mark",
    ],
    False: [
        "money_with_wings",
        "persevere",
        "sweat",
        "sob",
        "scream",
        "face_with_head_bandage",
        "skull",
        "poop",
        "see_no_evil",
        "scream_cat",
        "man-gesturing-no",
        "woman-gesturing-no",
        "man-shrugging",
        "woman-shrugging",
        "man-facepalming",
        "woman-facepalming",
        "facepunch",
        "third_place_medal",
        "moyai",
        "no_entry",
        "no_entry_sign",
        "heavy_multiplication_x",
        "x",
        "negative_squared_cross_mark",
    ]
}


def get_random_emoji(is_positive):
    """Pick a random positive or negative emoji based on is_positive flag."""

    return random.choice(emojis[is_positive])
