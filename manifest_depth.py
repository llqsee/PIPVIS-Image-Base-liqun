import os
import json

# GitHub raw base path
base_url = "https://raw.githubusercontent.com/piyushmohan01/PIPVIS-Image-Base/master/Categorical-Depth"

# Local directory
root = r"./Categorical-Depth"

output_path = "manifest_depth.json"

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

            # filename pattern: frame_5530_depth_bbox_local.jpg
            try:
                frame_num = fname.split("_")[1]
            except IndexError:
                frame_num = fname

            frames[frame_num] = f"{base_url}/{subset}/{ped}/{fname}"

        # ped key stripped of _depth_local suffix for consistent lookup
        ped_id = ped.replace("_depth_local", "")
        manifest[subset][ped_id] = {"frames": frames}

with open(output_path, "w") as f:
    json.dump(manifest, f, indent=2)

print(f"Depth manifest saved → {output_path}")