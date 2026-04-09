<div align="center">

# 🛡️ SOC Alert Analyzer  

## 🧠 SOC Systems • Detection Engineering • Agentic Investigation

![Focus](https://img.shields.io/badge/Focus-SOC%20Analysis%20%7C%20Triage%20%7C%20Mapping-blue?style=for-the-badge)
![Approach](https://img.shields.io/badge/Approach-Alert%20→%20Triage%20→%20Mapping-success?style=for-the-badge)
![Tech](https://img.shields.io/badge/Tech-Python%20%7C%20MITRE%20ATT%26CK%20%7C%20SOC-black?style=for-the-badge)

</div>

<div align="center">
  <img src="screenshots/soc_batch_summary.png" width="900">
</div>

<p align="center"><em>SOC batch summary showing alert distribution, MITRE mapping, and correlation.</em></p>

---

## 🧠 Purpose

This project represents the **alert analysis and triage stage** of an evolving SOC system.

| Stage | Description |
|------|------------|
| Alert Analysis | Understanding and triaging security events |
| Detection Engineering | Mapping behavior to MITRE ATT&CK |
| Investigation | Correlating and enriching alerts |
| Decision Support | Recommending response actions |

---

## 🎯 Objective

The goal of this phase is to demonstrate:

- how alerts are parsed and analyzed  
- how severity and confidence are assigned  
- how activity maps to MITRE ATT&CK  
- how correlation improves context  
- how structured triage supports downstream detection and investigation  

---

## 🔍 Phase 1 — SOC Alert Analyzer

![Focus](https://img.shields.io/badge/Focus-Triage%20%7C%20Analysis-blue)

| Category | Details |
|---------|--------|
| Focus | Alert parsing and triage |
| Role | SOC analyst simulation |
| Output | Structured alert analysis |

---

## 🧩 Key Capabilities

- alert parsing  
- severity scoring  
- MITRE ATT&CK mapping  
- response recommendations  
- multi-alert correlation  
- investigation validation  
- optional AI enrichment  

---

## 🧠 SOC Triage Workflow

| Stage | Description |
|------|------------|
| 🟦 Raw Alert | Alert ingestion from SIEM |
| 🟨 Triage | Severity and confidence scoring |
| 🧠 MITRE Mapping | Technique identification |
| ⚙️ Response Recommendation | Suggested actions |
| 📊 Correlation | Multi-alert context |
| 🔎 Investigation | Validation (e.g., Nmap) |
| 🤖 AI Enrichment | Optional enhancement |
| 📈 SOC Summary | Aggregated visibility |

---

## ⚡ Quick Start (Run the Project)

Run the SOC alert analyzer locally.

### 1. Clone the repository

```bash
git clone https://github.com/shannonasmith/AI-Assisted-SOC-Alert-Analyzer.git
cd AI-Assisted-SOC-Alert-Analyzer
```

---

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the analyzer

```bash
python soc_analyzer.py
```

---

## 👀 What This Looks Like in Practice

This walkthrough demonstrates how alerts are transformed into structured SOC analysis through triage, mapping, and investigation.

---

### ⚙️ Step 1 — Alert Processing & Triage

<div align="center">
  <img src="screenshots/alert_001_analysis.png" width="700">
</div>

### 🔍 Analysis Performed

- severity calculation  
- MITRE ATT&CK mapping  
- confidence scoring  
- response recommendation  
- timeline reconstruction  

---

### 🧪 Step 2 — Multi-Alert Analysis

<div align="center">
  <img src="screenshots/alert_002_analysis.png" width="700">
</div>

<div align="center">
  <img src="screenshots/alert_003_analysis.png" width="700">
</div>

### 🧠 Observations

- alerts vary in severity and intent  
- correlation improves context  
- low-severity events may indicate early-stage activity  

---

### 📈 Step 3 — SOC Correlation & Summary

<div align="center">
  <img src="screenshots/soc_batch_summary.png" width="700">
</div>

### 📊 Output Includes

- total alerts processed  
- severity breakdown  
- MITRE ATT&CK distribution  
- source IP correlation  
- repeat offender detection  

---

### 🔍 Step 4 — Investigation & Validation

<div align="center">
  <img src="screenshots/nmap_scan.png" width="700">
</div>

### 🔎 Findings

- host active  
- port 53 open (DNS)  

---

### 🤖 Step 5 — AI Enrichment Attempt

<div align="center">
  <img src="screenshots/soc_analyzer_output.png" width="700">
</div>

### 🧠 Insight

- rule-based logic remains reliable  
- AI enhances analysis but is not required  

---

## 🔍 SOC Analysis Workflow

```text
Alert Generation
    ↓
Rule-Based Triage
    ↓
MITRE Mapping
    ↓
Response Recommendation
    ↓
Multi-Alert Correlation
    ↓
Investigation
    ↓
AI Enrichment (Optional)
    ↓
SOC Summary
```

---

## 💡 What This Project Demonstrates

- SOC alert triage workflows  
- MITRE ATT&CK mapping  
- correlation and investigation  
- structured analysis pipelines  
- AI-assisted enrichment  

---

## 💼 SOC Relevance

Simulates:

- Tier 1 SOC triage  
- alert prioritization  
- initial investigation workflows  
- analyst decision-making  

---

## 🧬 Project Progression

This project is part of a **multi-phase SOC system**:

**SOC Alert Analyzer (current)** → [ATT&CK Mapping Engine](https://github.com/shannonasmith/AI-Assisted-SOC-MITRE-ATTACK-Mapping-Engine) → [Agentic SOC Investigation Engine](https://github.com/shannonasmith/Agentic-SOC-Investigation-Engine)

---

## 🚧 Future Work

- integration with detection engine (Phase 2)  
- improved correlation logic  
- expanded enrichment  
- structured output standardization  

---

<div align="center">

## 👤 Shannon Smith  

Cybersecurity | Threat Detection • Incident Response • Security Operations  

</div>
