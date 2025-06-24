# Data Ignition Anomaly Lab

A demonstration of time-series anomaly detection and predictive modeling built during the NICD Data Innovation Bootcamp (2025) by Group 8 – **Data Ignition Lab**. This repository showcases a prototype pipeline for identifying and predicting anomalies in operational temperature data from real-world sensor systems.

> **Note:** This repository is strictly for **demonstration purposes**. It is **not** intended for replication, deployment, or open data experimentation due to the proprietary nature of the original dataset and domain-specific insights.

---

## Problem Statement

_Add a short problem statement here – what the business challenge was, and why it mattered._  
_E.g., "Identify early signs of thermal risk or system overheating in battery infrastructure using unsupervised and supervised anomaly detection techniques."_  

---

## Project Overview

This notebook-based project explores an end-to-end anomaly detection framework involving:

- **Extreme Value Theory (EVT)**-based statistical anomaly detection
- **Rolling statistics & engineered features**
- **Predictive modeling using Random Forests**
- **Temporal anomaly visualization and probability thresholding**

The pipeline follows a robust approach to detect operational anomalies and model near-term risks, demonstrating practical ML under real-world constraints such as limited labels, noisy data, and time limitations.

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

data-ignition-anomaly-lab/
├── notebook.ipynb # Main Jupyter notebook
├── utils.py # Helper functions (e.g., for redaction)
├── .env # Local variables (excluded)
├── .gitignore # Prevents committing sensitive files
├── detected_anomalies.csv # Sample output (anonymized)
└── README.md # You're here!


---

## License

This repository is licensed under the [MIT License](LICENSE).

---

## Contributors

> _Note: Full contributor list to be added_

- _Your Name Here_ — Implementation, custom modeling, post-analysis author
- _[Add Original Team Members Here]_ — Original idea, data access, domain guidance

---

## Disclaimer

This repository includes code and ideas originally developed as part of a collaborative project during the NICD Data Innovation Bootcamp. While the implementation, documentation, and enhancements presented here were authored by me, **much of the foundational design, domain knowledge, and data access was made possible by contributions from other team members and stakeholders**.

Please treat this repository as a **demonstration of technical capability** and **not as a plug-and-play solution**.

---
