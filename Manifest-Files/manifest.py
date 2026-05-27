import os
import json

# base_url = "https://raw.githubusercontent.com/llqsee/PIPVIS-Image-Base-liqun/master/Bounding-Box"
base_url = "datasets/Bounding-Box"
root = r"./Bounding-Box"

output_path = "./Manifest-Files/manifest.json"

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

            # filename pattern: frame_5530.jpg
            try:
                frame_num = fname.split("_")[1].split(".")[0]
            except IndexError:
                frame_num = fname

            frames[frame_num] = f"{base_url}/{subset}/{ped}/{fname}"

        # no suffix to strip — ped folder name is the bare ped_id (e.g. 3_2_290)
        manifest[subset][ped] = {"frames": frames}

with open(output_path, "w") as f:
    json.dump(manifest, f, indent=2)

print(f"Bounding-box manifest saved → {output_path}")