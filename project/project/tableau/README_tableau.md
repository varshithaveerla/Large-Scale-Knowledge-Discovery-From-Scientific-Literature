# Tableau Dashboards – Large-Scale Knowledge Discovery

## Overview
This document describes the Tableau dashboards developed as part of the project  
**“Large-Scale Knowledge Discovery from the Enron Bag-of-Words Corpus Using Distributed PySpark Analytics and Scalable Machine Learning.”**

The dashboards translate large-scale text mining and distributed machine learning results into clear, interpretable, and actionable visual insights.

---

## Dataset Description
The dashboards are built on aggregated datasets derived from the Enron Bag-of-Words corpus.

Original schema:
- doc_id – Document identifier  
- word_id – Word identifier  
- count – Term frequency  

Aggregations were performed to ensure Tableau performance and usability.

---

## Dashboard 1: Data Quality and Pipeline Monitoring
**Purpose:** Validate data integrity and preprocessing effectiveness.

**Key Insights:**
- Realistic document length distributions
- Stable vocabulary growth
- Absence of ingestion anomalies

---

## Dashboard 2: Model Performance and Feature Importance
**Purpose:** Evaluate clustering quality and document structure.

**Key Insights:**
- Balanced cluster sizes
- Distinct document characteristics across clusters
- Interpretable feature patterns

---

## Dashboard 3: Business Insights and Recommendations
**Purpose:** Convert text analytics into actionable insights.

**Key Insights:**
- Dominant terms drive most content
- Clear separation between common and niche vocabulary
- Efficient keyword prioritization

---

## Dashboard 4: Scalability and Cost Analysis
**Purpose:** Analyze performance and cost trade-offs.

**Key Insights:**
- Strong initial scaling with diminishing returns
- Identification of optimal parallelism
- Balanced cost–performance configuration

---

## Tools Used
- Tableau Desktop
- PySpark
- Python

---

## Author
