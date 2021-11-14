import argparse
import re
from typing import List, Union, Iterable

from PIL import Image
from pathlib import Path

A4_WIDTH_INCHES = 8.27
A4_HEIGHT_INCHES = 11.7


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        help="A folder with input images and nothing else.",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Filename for the output PDF.",
        required=True,
    )
    parser.add_argument(
        "--dpi",
        help="DPI to use.",
        required=False,
        type=int,
        default=300,
    )
    parser.add_argument(
        "--image_w",
        help="Width of an individual image, in inches.",
        required=False,
        type=float,
        default=2.5,
    )
    parser.add_argument(
        "--image_h",
        help="Height of an individual image, in inches.",
        required=False,
        type=float,
        default=3.5,
    )
    args = parser.parse_args()
    return args


def combine_images_to_a4_pdf(
    input_path: Path,
    output_file: Path,
    dpi: int,
    image_w: float = 2.5,
    image_h: float = 3.5,
    margin: float = 10.0 / 300,
):
    """Combine images in input_path to multi-page PDF, try layout as many to a page as possible

    :param input_path: path with input images
    :param output_file: path for PDF to output
    :param dpi: DPI to use, eg 300
    :param image_w: width of an individual image, in inches
    :param image_h: height of an individual image, in inches
    :param margin: margin to use between images, in inches
    :return:
    """
    # scale margin to pixels
    margin = int(margin * dpi)
    # Size of one PDF page.
    width, height = int(A4_WIDTH_INCHES * dpi), int(A4_HEIGHT_INCHES * dpi)
    # Size of one image (defaults are a poker card)
    card_w, card_h = int(image_w * dpi), int(image_h * dpi)
    images = load_images(input_path)
    images_per_page = int(width / (card_w + 2 * margin)) * int(
        height / (card_h + 2 * margin)
    )
    output_file.parent.mkdir(parents=True, exist_ok=True)

    groups = [
        images[i : i + images_per_page] for i in range(0, len(images), images_per_page)
    ]
    for i, group in enumerate(groups):
        page = Image.new("RGB", (width, height), "white")
        x, y = margin, margin
        for img_file in group:
            img = Image.open(img_file).resize((card_w, card_h))
            page.paste(img, box=(x, y))
            x += img.size[0] + margin
            if x + img.size[0] + margin >= width:
                x = margin
                y += img.size[1] + margin
        page.save(output_file, append=(i > 0))


def load_images(input_path: Path) -> List[Path]:
    images = nat_sort_files(
        file for file in input_path.iterdir()
        if file.is_file() and not file.name.startswith(".")
    )
    return images


def nat_sort_files(paths: Iterable[Path]) -> List[Path]:
    """
    Primitive natural sorting of files (Path objects)

    :param paths: An iterable of paths.
    :return: A sorted list of Paths.
    """
    digit_pattern = re.compile(r"([0-9]+)")

    def convert_digits_to_ints(t: str) -> Union[int, str]:
        if t.isdigit():
            return int(t)
        else:
            return t

    def key(k: Path) -> List[Union[str, int]]:
        return [
            convert_digits_to_ints(part)
            for part in re.split(digit_pattern, k.stem)
        ]

    return sorted(paths, key=key)


def main():
    args = parse_args()
    combine_images_to_a4_pdf(
        Path(args.input),
        Path(args.output),
        args.dpi,
        args.image_w,
        args.image_h,
    )
    return 0


if __name__ == "__main__":
    main()
