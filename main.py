# One sentence (167 chars) explaining the modern internet to a traveler
# from 1800, built only from things they already know: road, post office,
# library, letter, book. No word coined after their time.
import os

SENTENCE = (
    "It is a road joining the post offices and libraries of many towns, "
    "so a letter you send can reach a friend across the sea and fetch "
    "a book from a far town in a breath."
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(SENTENCE)
