<div align="center">

## 🛡️ AI-Assisted SOC Alert Analyzer  
### SOC Triage, Correlation & AI-Assisted Investigation

![Category](https://img.shields.io/badge/Category-SOC%20Analysis-red?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Threat%20Detection-blue?style=for-the-badge)
![Tech](https://img.shields.io/badge/Tech-AI%20%2B%20MITRE-black?style=for-the-badge)

</div>

---

<div align="center">
  <img src="screenshots/soc_batch_summary.png" width="500">
</div>

<p align="center"><em>Figure 1. SOC batch summary showing alert distribution, MITRE mapping, and source correlation.</em></p>

---

## 🧠 Scenario

This project simulates how a **Security Operations Center (SOC)** processes and investigates alerts.

Instead of treating alerts as isolated events, this system demonstrates how analysts:

- triage alerts using structured logic  
- map activity to MITRE ATT&CK  
- correlate multiple signals  
- validate findings through investigation  
- attempt AI-assisted enrichment  

---

## 🎯 Objective

Build a workflow that reflects how SOC analysts move from:

- raw alerts  
→ structured triage  
→ investigation  
→ correlation  
→ decision-making  

---

## 🚨 Detection Perspective (SOC View)

From a SOC standpoint, the alerts represent:

- brute force attempts  
- reconnaissance / service discovery  
- low-volume authentication anomalies  

Each alert is evaluated for:

- severity  
- confidence  
- MITRE ATT&CK mapping  
- recommended response  

---

## 🖥️ Environment

| Tool | Purpose |
|---|---|
| Python | Alert processing engine |
| Kali Linux | Testing environment |
| Nmap | Investigation / validation |
| MITRE ATT&CK | Technique mapping |
| Google Gemini API | AI enrichment (attempted) |

---

## ⚙️ Step 1 — Alert Processing & Triage

<div align="center">
  <img src="screenshots/alert_001_analysis.png" width="600">
</div>

<p align="center"><em>Figure 2. Example alert analysis showing severity scoring, MITRE mapping, and response recommendation.</em></p>

### 🔍 Analysis Performed

- severity calculation  
- MITRE ATT&CK mapping  
- confidence scoring  
- response recommendation  
- timeline reconstruction  

---

## 🧪 Step 2 — Multi-Alert Analysis

<div align="center">
  <img src="screenshots/alert_002_analysis.png" width="600">
</div>

<p align="center"><em>Figure 3. High-severity reconnaissance activity mapped to T1046.</em></p>

<div align="center">
  <img src="screenshots/alert_003_analysis.png" width="600">
</div>

<p align="center"><em>Figure 4. Low-severity authentication anomaly mapped to T1078.</em></p>

### 🧠 Observations

- alerts vary in severity and intent  
- correlation improves context  
- low-severity events may indicate early-stage activity  

---

## 📈 Step 3 — SOC Correlation & Summary

<div align="center">
  <img src="screenshots/soc_batch_summary.png" width="500">
</div>

<p align="center"><em>Figure 5. Aggregated SOC view showing severity distribution and MITRE coverage.</em></p>

### 📊 Output Includes

- total alerts processed  
- severity breakdown  
- MITRE ATT&CK distribution  
- source IP correlation  
- repeat offender detection  

➡️ Alert-level → **situational awareness**

---

## 🔍 Step 4 — Investigation & Validation

<div align="center">
  <img src="screenshots/nmap_scan.png" width="600">
</div>

<p align="center"><em>Figure 6. Nmap scan validating exposed service.</em></p>

### 🔎 Findings

- host active  
- port 53 open (DNS)  

➡️ Confirms reconnaissance behavior  

---

## 🤖 Step 5 — AI Enrichment Attempt

<div align="center">
  <img src="screenshots/soc_analyzer_output.png" width="600">
</div>

<p align="center"><em>Figure 7. AI model failure due to quota limits.</em></p>

### 🧠 Analysis

- rule-based logic still succeeded  
- AI is enrichment, not dependency  

---

## 🔧 Step 6 — Development & Troubleshooting

### Environment Setup

<div align="center">
  <img src="screenshots/development_workflow.png" width="600">
</div>

<p align="center"><em>Figure 8. Virtual environment and dependency installation.</em></p>

---

### Execution Validation

<div align="center">
  <img src="screenshots/ai_analysis_output.png" width="600">
</div>

<p align="center"><em>Figure 9. File validation and script setup.</em></p>

---

### Debugging Example

<div align="center">
  <img src="screenshots/debugging_example.png" width="600">
</div>

<p align="center"><em>Figure 10. Execution error due to incorrect filename.</em></p>

---

## 🧠 Attack Flow (SOC Perspective)

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
    Investigation (Nmap)
    ↓
    AI Enrichment (attempted)
    ↓
    SOC Summary

---

## 🛠️ Techniques Demonstrated

- brute force detection (T1110)  
- network discovery detection (T1046)  
- account-based monitoring (T1078)  
- alert correlation  
- investigation validation  
- AI-assisted analysis  

---

## 🛡️ Response (SOC Perspective)

### Containment
- monitor suspicious IPs  
- isolate systems  
- block sources  

### Investigation
- validate services  
- analyze authentication  

### Monitoring
- track login attempts  
- detect recon behavior  

---

## 📊 Key Takeaways

- structured triage enables consistency  
- correlation improves visibility  
- investigation validates alerts  
- AI enhances analysis, not replaces it  

---

## 💡 Skills Demonstrated

- SOC alert triage  
- MITRE ATT&CK mapping  
- threat analysis  
- investigation techniques  
- troubleshooting  
- AI-assisted workflows  

---

<div align="center">

## 👤 Shannon Smith

Cybersecurity | Threat Detection • Incident Response • Security Operations  
U.S. Navy Veteran | Virginia Tech — M.S. Information Technology  

🧠 Structured analysis  
🔍 Investigation-driven validation  
🛡️ Real-world SOC workflow simulation  

</div>
