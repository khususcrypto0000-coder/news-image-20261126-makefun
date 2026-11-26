"""Copy the entry image to the output directory.

Stdlib only, no network. Running this program twice produces the
exact same bytes at /output/entry.png every time.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "output", "entry.png")
    dst = "/output/entry.png"
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)
    print("Wrote {} ({} bytes)".format(dst, os.path.getsize(dst)))


if __name__ == "__main__":
    main()
