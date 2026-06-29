import os
import json

# === CONFIGURATION ===
# GitHub raw base path for Full-Scale images
# base_url = "https://raw.githubusercontent.com/piyushmohan01/PIPVIS-Image-Base/master/Full-Scale-Semantic"
# base_url = "datasets/Full-Scale-Semantic"
base_url = "https://huggingface.co/datasets/lqliu/pipvis/resolve/main/Full-Scale-Semantic"

# Local directory where your Full-Scale frames are stored
root = r"./Full-Scale-Semantic"

output_path = "./Manifest-Files/manifest_full_sem.json"

manifest = {}

# Check if root exists to prevent errors
if not os.path.exists(root):
    print(f"Error: Directory {root} not found.")
else:
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

            # Sort files to ensure numerical order in the JSON
            for fname in sorted(os.listdir(ped_dir)):
                if not fname.lower().endswith(".jpg"):
                    continue

                # filename pattern: frame_5530_sem_bbox_full.jpg
                try:
                    # Extracts '5530' from the filename
                    frame_num = fname.split("_")[1]
                except IndexError:
                    frame_num = fname

                # Construct the full GitHub URL
                frames[frame_num] = f"{base_url}/{subset}/{ped}/{fname}"

            # Strip '_full_scale' suffix to create a clean ped_id (e.g., 3_2_290)
            ped_id = ped.replace("_full", "")
            manifest[subset][ped_id] = {"frames": frames}

    # Save the generated manifest
    with open(output_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"Full-Scale Semantic manifest saved → {output_path}")