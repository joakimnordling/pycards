from PIL import Image, ImageDraw, ImageFont, ImageOps


# create huge global dict that has all assets
ASSET_SIZE_HUGE = (150, 150)
ASSET_SIZE_BIG = (65, 65)
ASSET_SIZE = (50, 50)
ASSET_SIZE_SMALL = (35, 35)
ASSETS = {
    'artisan': Image.open("assets/artisan.png").resize(ASSET_SIZE, Image.BILINEAR),
    'blood_small': Image.open("assets/blood.png").resize(ASSET_SIZE_SMALL, Image.BILINEAR),
    'blood': Image.open("assets/blood.png").resize(ASSET_SIZE_BIG, Image.BILINEAR),
    'blood_big': Image.open("assets/blood.png").resize(ASSET_SIZE_HUGE, Image.BILINEAR),
    'farmer': Image.open("assets/farmer3.png").resize(ASSET_SIZE, Image.BILINEAR),
    'influence': Image.open("assets/trophy.png").resize(ASSET_SIZE_BIG, Image.BILINEAR),
    'influence_big': Image.open("assets/trophy.png").resize(ASSET_SIZE_HUGE, Image.BILINEAR),
    'neg_influence_small': Image.open("assets/death-skull.png").resize(ASSET_SIZE_SMALL, Image.BILINEAR),
    'neg_influence': Image.open("assets/death-skull.png").resize(ASSET_SIZE_BIG, Image.BILINEAR),
    'noble': Image.open("assets/crown2.png").resize(ASSET_SIZE, Image.BILINEAR),
    'philosopher': Image.open("assets/philosopher.png").resize(ASSET_SIZE, Image.BILINEAR),
    'slave': Image.open("assets/manacles.png").resize(ASSET_SIZE_BIG, Image.BILINEAR),
    'soldier': Image.open("assets/soldier.png").resize(ASSET_SIZE, Image.BILINEAR),
    'soldier_big': Image.open("assets/soldier.png").resize(ASSET_SIZE_HUGE, Image.BILINEAR),
    'sword': Image.open("assets/sword.png").resize(ASSET_SIZE, Image.BILINEAR),
    'sword_small': Image.open("assets/sword.png").resize(ASSET_SIZE_SMALL, Image.BILINEAR),
    'trimeme': Image.open("assets/trimeme3.png").resize(ASSET_SIZE, Image.BILINEAR),
}
# generate fonts
# fonts: https://www.urbanfonts.com/fonts/greek-fonts.htm
FONT_FILE = "assets/GRECOromanLubedWrestling.ttf"
ASSETS['font_file'] = FONT_FILE
ASSETS['font_name'] = ImageFont.truetype(FONT_FILE, size=40)
ASSETS['font_body'] = ImageFont.truetype(FONT_FILE, size=30)
