# Coolest art — make.fun entry

A majestic phoenix with blazing orange, gold and crimson feathers rising
from glowing embers, wings spread wide, sparks swirling, against a dark
nebula sky in deep purple and teal. The entry program copies the image to
`/output/entry.png`.

## Files

- `main.py` — the entry program (Python 3.13, standard library only).
  Copies `art.jpg` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`).
- `art.jpg` — the phoenix artwork (JPEG, 1024x1024, 322,133 bytes).
  The output keeps the name `entry.png`; the format is told apart by its
  first bytes, as the competition rules allow.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Two runs write byte-identical output (a plain file copy).
