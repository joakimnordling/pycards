""" Generate "blood" card images from card specification in CSV
"""
from pathlib import Path
from typing import List

from PIL import Image, ImageDraw
from pycards.gsheets import download_gsheets
from pycards.render import render_text_with_assets

from renderable_card import make_renderable_card


# Cards are defined in this Google sheet
CARD_SHEET_ID = "1Q8gs-XEURbsVB43OSe1DDL_W3T7tPryzOr-oUkxydbE"
CARD_SHEET_NAME = "Blood_cards"
OUTPUT_PATH = Path("data/blood_cards")


def load_card_data() -> List[dict]:
    cards_df = download_gsheets(CARD_SHEET_ID, CARD_SHEET_NAME)
    print("printing the cards")
    print(cards_df)
    cards = cards_df.to_dict("records")
    return cards


def render_line(card, rxy, text):
    img = card["_img"]
    font = card["_assets"]["font_body"]
    render_text_with_assets(
        rxy,
        text=text,
        img=img,
        font=font,
        text_color=card["_colors"]["fill"],
        assets=card["_assets"],
        align="center",
        max_width=1.0,
    )


def render_card(card):
    img = Image.new("RGB", card["_size"], color=card["_colors"]["empire"])
    draw = ImageDraw.Draw(img)
    card["_img"] = img
    card["_draw"] = draw
    render_line(card, (0.5, 0.38), text=card["First line"])
    render_line(card, (0.5, 0.62), text=card["Second line"])


def main():
    cards = load_card_data()
    rcards = [make_renderable_card(card) for card in cards]
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
    i = 1
    for card in rcards:
        for _ in range(0, card["Card count"]):
            render_card(card)
            img = card["_img"]
            img.save(OUTPUT_PATH / f"card_{i}.png", "PNG")
            i += 1

    # Render card back images
    back_cards = [x for x in rcards if x["Card count"] < 0]
    for card in back_cards:
        render_card(card)
        img = card["_img"]
        back_output_path = OUTPUT_PATH.parent
        filename = card["File"]
        img.save(back_output_path / filename, "PNG")


if __name__ == "__main__":
    main()
