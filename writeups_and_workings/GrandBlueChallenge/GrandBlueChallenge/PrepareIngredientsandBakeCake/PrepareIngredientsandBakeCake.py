#!/usr/bin/env python3
"""
Extract a steganographically stored payload image from a carrier image
"""
import click
import imageio
import numpy as np
from PIL import Image


def extract_lsb(image):
    lsbs = image.flatten() & 1
    width = np.packbits(lsbs[:8])[0].astype(int)
    height = np.packbits(lsbs[8:16])[0].astype(int)
    num_payload_bits = width * height * 8 * 3
    payload_bits = lsbs[16 : 16 + num_payload_bits]
    payload = np.packbits(payload_bits).reshape(height, width, 3)
    return payload


def extract(image, method="lsb", **kwargs):
    method_map = {"lsb": extract_lsb}
    return method_map[method](image, **kwargs)


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.argument("left", required=True)
@click.argument("right", required=True)
@click.option("--output", default="extracted.png")
@click.option("--show", is_flag=True)
@click.option("--method", default="lsb")
def main(left, right, show, output, method):
    left = imageio.imread(left)
    right = imageio.imread(right)
    image = np.concatenate((left, right), axis=1)
    payload = extract(image, method=method)
    if show:
        Image.fromarray(payload).show()
    imageio.imwrite(output, payload)


if __name__ == "__main__":
    main()