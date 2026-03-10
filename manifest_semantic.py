import os
import json

# GitHub raw base path
base_url = "https://raw.githubusercontent.com/piyushmohan01/PIPVIS-Image-Base/master/Semantic-Segmentation-Frames"

# Local directory
root = r"./Semantic-Segmentation-Frames"

output_path = "manifest_semantic.json"

manifest = {}

for subset in os.listdir(root):
    subset_dir = os.path.join(root, subset)

    if not os.path.isdir(subset_dir):
        continue

    manifest[subset] = {}

    for ped in os.listdir(subset_dir):
        ped_dir = os.path.join(subset_dir, ped)

        if not os.path.isdir(ped_dir):
            continue

        frames = {}

        for fname in sorted(os.listdir(ped_dir)):

            if not fname.lower().endswith(".jpg"):
                continue

            # expected filename: frame_5539_sem_bbox.jpg
            try:
                frame_num = fname.split("_")[1]
            except IndexError:
                frame_num = fname

            frames[frame_num] = f"{base_url}/{subset}/{ped}/{fname}"

        manifest[subset][ped] = {"frames": frames}


# write manifest
with open(output_path, "w") as f:
    json.dump(manifest, f, indent=2)

print(f"Semantic manifest saved → {output_path}")