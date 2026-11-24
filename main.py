"""Copy the day's news image to the output directory.

The image itself is the entry: it was composed for Tuesday 24 November
2026 (masthead, hero illustration, six story cards). This program only
places the finished file where the grader reads it, byte for byte.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(OUT, "entry.png"))
