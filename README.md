# PIPVIS Image Base

Supporting image repository for the **PIPVIS Dashboard** — an interactive visualisation and interpretability system for pedestrian intention prediction (PIP) models.

---

## Dashboard

The PIPVIS dashboard is built in Observable/D3.js and uses this repository as its image hosting backend.

🔗 **[View the PIPVIS Dashboard](https://observablehq.com/d/41ea89895dd12b44)**

### Demo

https://github.com/piyushmohan01/PIPVIS-Image-Base/blob/master/PIPVIS-Dashboard-Demo.mp4

[Demo][https://raw.githubusercontent.com/piyushmohan01/PIPVIS-Image-Base/blob/master/PIPVIS-Dashboard-Demo.mp4

]

---

## Repository Structure

```
PIPVIS-Image-Base/
│
├── Bounding-Box/ # Local context — bbox overlay (224×224)
│   └── {subset}/{ped_id}/
│
├── Body-Pose/ # Local context — body pose overlay (224×224)
│   └── {subset}/{ped_id}/
│
├── Optical-Flow/ # Local context — RAFT optical flow (224×224)
│   └── {subset}/{ped_id}_flow_local/
│
├── Categorical-Depth/ # Local context — Categorical depth (224×224)
│   └── {subset}/{ped_id}_depth_global/
│
├── Full-Scale-BBox/ # Full-scale RGB frame with bbox
│   └── {subset}/{ped_id}_full_scale/
│
├── Full-Scale-Semantic/ # Full-scale semantic segmentation
│   └── {subset}/{ped_id}_full/
│
├── manifest.json               # Bounding Box image URLs
├── manifest_pose.json          # Body Pose image URLs
├── manifest_flow.json          # Optical Flow image URLs
├── manifest_depth.json         # Categorical Depth image URLs
├── manifest_full.json          # Full-Scale RGB image URLs
└── manifest_full_sem.json      # Full-Scale Semantic image URLs
```

**Subsets:** `FN` (False Negatives) · `FP` (False Positives) · `TP` (True Positives) · `TN` (True Negatives)

---

## Manifests

JSON file mapping `subset → ped_id → frame_number → image URL`.

```json
{
  "FN": {
    "3_2_290": {
      "frames": {
        "5530": "https://raw.githubusercontent.com/.../frame_5530_bbox.jpg",
        "5531": "https://raw.githubusercontent.com/.../frame_5531_bbox.jpg"
      }
}}}
```

| Manifest | Image Type | Local / Full | Size |
|---|---|---|---|
| `manifest.json` | Bounding Box | Local | 224×224 |
| `manifest_pose.json` | Body Pose | Local | 224×224 |
| `manifest_flow.json` | Optical Flow (RAFT) | Local | 224×224 |
| `manifest_depth.json` | Categorical Depth | Local | 224×224 |
| `manifest_full.json` | RGB Full-Scale | Full | Original |
| `manifest_full_sem.json` | Semantic Segmentation Full-Scale | Full | Original |

---

## Dataset & Model

Images are derived from the **[PIE Dataset](http://data.nvision2.eecs.yorku.ca/PIE_dataset/)** (Pedestrian Intention Estimation) and processed through the **PIP-Net** model pipeline.

---

## Project

PIPVIS is funded by **MAVIS** (EPSRC EP/X029689/1) and **Hi-Drive** (EU Horizon 2020, grant 101006664), developed at the **Leeds Institute for Data Analytics (LIDA), University of Leeds**.

Team:
- Piyush Mohan (Lead Data Scientist)
- Dr. Mahdi Rezaei (Lead Supervisor, PIP Expert)
- Prof. Roy Ruddle (Supervisor, XAI Vis Expert)
- Mohsen Azarmi (Team Member, PIP Expert)
- Dr. Liqun Liu (Team Member, XAI Vis Expert)
- Dr. Patrizia Franco (External Partner, SYSTRA UK & Ireland)

---

## Related

- 📄 Paper accepted for **Digital Footprints 2026**
- 💻 Dashboard source: [Observable notebook](https://observablehq.com/d/41ea89895dd12b44)
