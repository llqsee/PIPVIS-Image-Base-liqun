import os
import json

# base_url = "https://raw.githubusercontent.com/piyushmohan01/PIPVIS-Image-Base/master/Body-Pose"
base_url = "datasets/Body-Pose"
root = r"./Body-Pose"

output_path = "./Manifest-Files/manifest_pose.json"

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

            # filename pattern: frame_5530_pose.jpg
            try:
                frame_num = fname.split("_")[1]
            except IndexError:
                frame_num = fname

            frames[frame_num] = f"{base_url}/{subset}/{ped}/{fname}"

        # no suffix to strip — ped folder name is the bare ped_id (e.g. 3_2_290)
        manifest[subset][ped] = {"frames": frames}

with open(output_path, "w") as f:
    json.dump(manifest, f, indent=2)

print(f"Body-pose manifest saved → {output_path}")