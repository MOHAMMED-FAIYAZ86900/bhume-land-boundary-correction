# BhuMe Land Boundary Correction Assignment

## Overview

This project addresses the problem of correcting misaligned cadastral plot boundaries using satellite imagery and land records.

Many official cadastral boundaries are spatially shifted due to errors introduced during digitization and georeferencing of historical village maps. The objective is to identify plots whose boundaries can be corrected and estimate improved positions while flagging uncertain cases.

---

# Dataset

Village: Vadnerbhairav, Nashik

Provided Data:

* input.geojson (official cadastral plots)
* imagery.tif (satellite imagery)
* boundaries.tif (rough field-boundary hints)
* example_truths.geojson (manually corrected sample plots)

Total plots: 2457

---

# Approach

## 1. Data Exploration

The cadastral GeoJSON was analyzed to understand:

* Plot geometries
* Recorded area
* Map area
* Survey information
* Area discrepancies

Area ratio was computed:

area_ratio = map_area_sqm / recorded_area_sqm

This helped distinguish potential placement errors from area-definition errors.

---

## 2. Drift Analysis

Using the provided example_truths.geojson, centroid shifts between official boundaries and corrected boundaries were measured.

Observed shifts revealed a consistent village-level drift pattern.

Average drift estimate:

DX ≈ -0.000051

DY ≈ 0.000110

This global shift was used as the first correction model.

---

## 3. Edge Detection

Satellite image patches were extracted for individual plots.

Canny Edge Detection was applied:

* Convert RGB image to grayscale
* Gaussian blur
* Canny edge extraction

This was used to identify visible field boundaries from imagery.

---

## 4. Alignment Framework

Implemented components:

* Polygon mask generation
* Alignment scoring
* Candidate shift search
* Confidence estimation

These components provide the basis for future local boundary refinement.

---

## 5. Boundary Correction

A global correction model was applied:

* Translate plot geometry by estimated drift
* Generate corrected geometry
* Preserve original geometry for uncertain cases

---

## 6. Confidence Estimation

Confidence was derived from consistency between:

* Recorded area
* Map area

Plots with strong area agreement received higher confidence.

Plots with low confidence were flagged instead of corrected.

---

## 7. Decision Logic

If confidence ≥ threshold:

Status = corrected

Else:

Status = flagged

This introduces restraint and prevents over-correction of uncertain plots.

---

# Results

Example Truth Evaluation

Official Median IoU: 0.612

Corrected Median IoU: 0.704

Improvement: +0.126

Improved Plots: 100%

Accurate (IoU ≥ 0.5): 100%

Confidence Correlation (Spearman): 0.393

Prediction Summary:

* Corrected plots: 2133
* Flagged plots: 324

---

# Repository Structure

src/

* predictor.py
* corrector.py
* confidence.py
* edges.py
* alignment.py
* search.py
* mask_utils.py
* geometry_utils.py
* process_plot.py

Root Files:

* generate_predictions.py
* score_global.py
* README.md

Output:

* predictions.geojson

---

# Running the Project

Generate predictions:

python generate_predictions.py

Evaluate predictions:

python score_global.py

---

# Output Format

The generated predictions.geojson follows the assignment specification:

Fields:

* plot_number
* status
* confidence
* method_note
* geometry

Coordinate System:

EPSG:4326

---

# Future Improvements

Potential extensions include:

* Local edge-based refinement
* Adaptive shift estimation
* Neighbor-aware correction
* Learned boundary alignment
* Improved confidence calibration

---

# AI Usage

AI tools were used during development for:

* Assignment understanding
* Geospatial workflow planning
* Drift analysis
* Confidence design
* Code generation assistance
* Evaluation workflow

All implementation decisions, testing, debugging, and final integration were performed manually.
