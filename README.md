# Data Ignition Lab - Anomaly Detection

A demonstration of time-series anomaly detection and predictive modeling built during the NICD Data Innovation Bootcamp (2025) by Group 8 – **Data Ignition Lab**. This repository showcases a prototype pipeline for identifying and predicting anomalies in operational temperature data from real-world sensor systems.

> **Note:** This repository is strictly for **demonstration purposes**. It is **not** intended for replication, deployment, or open data experimentation due to the proprietary nature of the original dataset and domain-specific insights.

---

## About Connected Energy

<p>The business was founded to approach anenergy, transport and environmental problem creatively driven by supporting the circular economy. As
the world strives towards net zero, our batteryenergystorage systems solve two majorenergychallenges: reliable storage for
renewableenergyand repurposing of electric vehicle batteries. Connected Energy is on a mission to help the world embrace sustainable energy solutions that
harnesses the value embedded in second life electric vehicle batteries. Based in the UK, but operating internationally, to provide
battery energy storage systems.</p>

## Problem Statement

<p>Connected Energy maintains battery energy storage systems at various locations around the UK and
Europe. These systems are continually monitored for performance and maintenance reasons. How can
connected energy make better use of the data collected to identify, predict and report issues to clients?</p>

---

### View the Notebook

You can view the notebook here: [Open in Google Colab](https://colab.research.google.com/drive/18OSQz5Fyk6_z0eKrAjBLeRY3MUhHhbAD?usp=sharing)

---

## Project Overview

This notebook-based project explores an end-to-end anomaly detection framework involving:

- **Extreme Value Theory (EVT)**-based statistical anomaly detection
- **Rolling statistics & engineered features**
- **Predictive modeling using Random Forests**
- **Temporal anomaly visualization and probability thresholding**

The pipeline follows an approach to detect operational anomalies and model near-term risks, demonstrating practical ML under real-world constraints such as limited labels, noisy data, and time limitations.

---

## Redaction & Masking

Since this work was based on confidential and proprietary business data:

- All direct identifiers have been **masked or redacted** (e.g., battery names replaced with `battery_01`)
- Only **aggregated statistics** and **summary outputs** are shared
- **No raw datasets** or business-specific references are included
- Environmental variable usage (`.env`) and keys have been **excluded from source control** (`.gitignore`)

---

## Why Redaction Was Necessary

This project was conducted in collaboration with an operational team in a real business setting. To respect NDAs, protect customer confidentiality, and align with ethical data practices, only a sanitized and partial version of the analysis pipeline is demonstrated.

> This ensures the work can be **shared publicly as a portfolio project** without disclosing sensitive operational knowledge.

---

## Key Findings (Sample)

Here are a few insights from the modeling and analysis:

- **Temperature anomalies** can be captured effectively using EVT-based methods
- A **Random Forest classifier** showed strong overall accuracy (~98%), though recall on minority (anomalous) cases remained modest (~38%)
- The probability threshold can be optimized using **Precision-Recall trade-offs**
- Temporal patterns (hour of day) contributed moderately to predictive power

---

## Conclusion

This project illustrates a scalable approach to anomaly detection in time-series data with minimal supervision. While built under tight timelines, it effectively balances interpretability, detection performance, and operational insights.

---

## Repository Structure

| File/Directory           | Description                              |
|--------------------------|------------------------------------------|
| `utils.py`               | Helper functions (e.g., for redaction)   |
| `plot_utils.py`          | Contains functions for generating time variation plots and interactive time series visualizations.|
| `thresholding.py`        | 	Implements an adaptive thresholding algorithm to detect anomalies in time series data.|
| `timer.py`               | Provides a context-based timer utility for measuring code execution time.              |
| `README.md`              | You're here!                            |

---

## Contributors

- [Samraat Jain](https://github.com/SamraatJain9) — Implementation, custom modeling, post-analysis author
- Paul Goodman (paul.goodman@newcastle.ac.uk) — Original analysis, data access, domain guidance

---

## Disclaimer

This repository includes code and ideas originally developed as part of a collaborative project during the NICD Data Innovation Bootcamp. While the implementation, documentation, and enhancements presented here were authored by me, **much of the foundational design, domain knowledge, and data access was made possible by contributions from other team members and stakeholders**.

Please treat this repository as a **demonstration of technical capability** and **not as a plug-and-play solution**.

---
