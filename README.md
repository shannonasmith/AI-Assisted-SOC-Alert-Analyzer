# 🛡️ AI-Assisted SOC Alert Analyzer

## 📌 Overview

This project simulates an **AI-assisted Security Operations Center (SOC) workflow** that processes security alerts, performs triage, maps activity to MITRE ATT&CK techniques, and generates incident analysis with recommended response actions.

The goal is to demonstrate how **AI can augment SOC analysts** by transforming raw alert data into structured, decision-ready insights.

---

## 🎯 Objectives

- Simulate real-world SOC alert triage
- Combine **rule-based detection** with **AI-assisted analysis**
- Map activity to **MITRE ATT&CK techniques**
- Demonstrate progression toward **agentic AI workflows**
- Build a reusable, modular Python-based analysis tool

---

## ⚙️ Features

### 🔍 Alert Processing
- Ingests alerts from a JSON file
- Supports multiple incident types:
  - Brute force attempts
  - Port scans
  - Authentication anomalies

### 🧠 Rule-Based Triage
- Severity scoring (High / Medium / Low)
- Confidence scoring
- MITRE ATT&CK mapping

### 📊 Investigation Context
- Timeline reconstruction for each alert
- Alert ID tracking
- Source IP correlation

### 🤖 AI-Assisted Analysis
- Uses a generative AI model (Gemini) to:
  - Summarize incidents
  - Validate severity
  - Suggest MITRE techniques
  - Recommend response actions

### ⚡ Decision + Response Layer
- Action recommendations based on severity
- Simulated response execution:
  - IP blocking
  - Host isolation
  - Monitoring actions

### 📈 Batch SOC Summary
- Total alerts processed
- Severity distribution
- MITRE ATT&CK coverage
- Source IP breakdown

---

## 🧱 Architecture

```text
alerts.json
↓
Rule-Based Triage (Severity + MITRE + Confidence)
↓
Decision Layer (Recommended Actions)
↓
Simulated Response
↓
Timeline Reconstruction
↓
AI Analysis (Context + Recommendations)
↓
Batch Summary
```

📸 **Architecture Diagram (optional)**  
![Architecture](screenshots/architecture.png)

---

## 📁 Project Structure

```text
mini-ai-soc/
├── soc_analyzer.py
├── alerts.json
├── output.log (optional)
├── screenshots/
│   ├── output.png
│   └── architecture.png
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/mini-ai-soc.git
cd mini-ai-soc
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install google-genai
```

### 4. Set API key

```bash
export GEMINI_API_KEY="your_api_key_here"
```

### 5. Run the analyzer

```bash
python soc_analyzer.py alerts.json
```

---

## 🧪 Example Alerts

```json
[
  {
    "id": "ALERT-001",
    "event": "Failed login attempts",
    "source_ip": "192.168.1.45",
    "target_user": "admin",
    "attempts": 15,
    "time_window": "2 minutes"
  },
  {
    "id": "ALERT-002",
    "event": "Port scan detected",
    "source_ip": "10.0.0.88",
    "target_user": "N/A",
    "attempts": 50,
    "time_window": "1 minute"
  }
]
```

---

## 📊 Example Output

```text
Processing Alert ID: ALERT-001

=== PRE-AI ANALYSIS ===
Calculated Severity: Medium
MITRE Mapping: T1110 - Brute Force
Confidence: Moderate Confidence

[ACTION] Recommend investigating source IP 192.168.1.45
[SIMULATION] Monitoring source IP 192.168.1.45

[Timeline Reconstruction]
- Initial Activity: Multiple failed logins detected
- Source: 192.168.1.45
- Target: admin
- Duration: 2 minutes
- Behavior: Repeated authentication attempts indicating possible brute force

[AI Analysis]
- Summary
- Severity adjustment
- Recommendations
```

📸 **Terminal Output Example**  
![Terminal Output](screenshots/output.png)

---

## 🧠 Key Concepts Demonstrated

- SOC alert triage workflows  
- MITRE ATT&CK mapping  
- AI-assisted incident analysis  
- Separation of deterministic logic and AI reasoning  
- Simulated SOAR-style response actions  

---

## 🔐 Security Perspective

This project demonstrates how modern SOCs can:

- Reduce alert fatigue through automation  
- Improve investigation speed using AI  
- Correlate alerts across multiple signals  
- Transition toward autonomous response systems  

---

## 🚧 Future Improvements

- Integrate real SIEM data (Splunk, ELK)  
- Connect to MITRE ATT&CK STIX dataset  
- Add real-time log ingestion  
- Implement automated SOAR playbooks  
- Export ATT&CK coverage to Navigator  

---

## 💡 Lessons Learned

- Combining rule-based logic with AI improves reliability  
- AI should assist—not replace—security decision-making  
- Context (timeline, source, behavior) is critical in incident response  
- API integration and model selection require careful validation  

---

## 👤 Author

Shannon Smith  
Cybersecurity | Threat Detection | Incident Response | Automation & AI
