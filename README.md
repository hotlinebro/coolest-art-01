# Phoenix Rising — Coolest Art

A phoenix rising from the embers, drawn in warm reds, oranges, and gold.

This entry pairs the phoenix artwork (`art.jpg`) with a small, deterministic
program (`main.py`) that copies the artwork to the output directory as
`entry.png`. Running it twice produces byte-identical output every time.

## How to run

```sh
python3 main.py
```

By default the output goes to the standard output directory (`/output`).
To write somewhere else, set the `MAKEFUN_OUTPUT_DIR` environment variable
before running, for example:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
