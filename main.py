"""Coolest Art entry: a phoenix rising.

This program copies the phoenix artwork to the output directory.
The result is a byte-exact copy of art.jpg. The output file is
still named entry.png, and its format is recognised from its
leading bytes, as the contest rules allow. This plain copy is
deterministic: two runs write identical bytes.
"""

import hashlib
import os
import shutil
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = Path(__file__).resolve().parent / "art.jpg"
DST = Path(OUTPUT_DIR) / "entry.png"


def main():
    # Salin gambar phoenix apa adanya, tanpa perubahan isi apa pun.
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    data = DST.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    print(f"{DST}: {len(data)} bytes, sha256={digest}")


if __name__ == "__main__":
    main()
