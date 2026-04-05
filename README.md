# 🛡️ AI-Assisted SOC Alert Analyzer

## 📌 Overview

This project simulates how a Security Operations Center (SOC) actually processes alerts — not just detecting them, but **triaging, investigating, and deciding what to do next**.

I built this to explore how **AI can assist (not replace)** a SOC analyst by adding context, validating decisions, and accelerating investigations.

Instead of treating alerts as isolated events, this project shows how multiple signals can be analyzed together to produce **meaningful, actionable insight**.

---

## 🎯 What This Project Demonstrates

- How SOC analysts triage alerts in real workflows  
- Mapping activity to **MITRE ATT&CK techniques**  
- Combining **rule-based logic + AI reasoning**  
- Moving toward **AI-assisted / agentic SOC workflows**  
- Turning raw alerts into **decision-ready output**

---

## ⚙️ How It Works

```text
alerts.json
↓
Rule-Based Triage (Severity + MITRE + Confidence)
↓
Recommended Actions
↓
Simulated Response
↓
Timeline Reconstruction
↓
AI Analysis
↓
Batch Summary + Correlation
```

---

## 📸 Project Walkthrough

### 🔴 1. Reconnaissance (Attack Simulation)

![Nmap Scan](screenshots/nmap_scan.png)

Simulated reconnaissance using Nmap.  
An exposed DNS service (port 53) was identified, demonstrating how attackers discover reachable services and potential entry points.

---

### ⚙️ 2. Initial SOC Triage

![SOC Analyzer](screenshots/soc_analyzer_output.png)

Each alert is first analyzed using deterministic logic:
- Severity scoring
- MITRE ATT&CK mapping
- Confidence scoring
- Initial response recommendations

---

### 🤖 3. AI-Assisted Analysis

![AI Analysis](screenshots/ai_analysis_output.png)

AI expands the investigation by:
- Summarizing the alert
- Validating or adjusting severity
- Suggesting additional attack context
- Recommending response actions

---

### 📊 4. Multi-Alert Analysis

#### ALERT-001 (Brute Force)

![Alert 1](screenshots/alert_001_analysis.png)

- Medium severity brute force attempt  
- Internal source targeting privileged account  

---

#### ALERT-002 (Port Scan / Recon)

![Alert 2](screenshots/alert_002_analysis.png)

- High severity reconnaissance activity  
- Triggered network service discovery detection  

---

#### ALERT-003 (Low-Level Auth Activity)

![Alert 3](screenshots/alert_003_analysis.png)

- Low severity event  
- Possible early-stage probing or benign failure  

---

### 📈 5. SOC Batch Summary

![Summary](screenshots/soc_batch_summary.png)

After processing multiple alerts, the system generates:

- Severity distribution  
- MITRE ATT&CK coverage  
- Source IP correlation  
- Repeat offender detection  

This reflects how analysts move from **individual alerts → overall situational awareness**

---

### 🧪 6. Development & Troubleshooting

![Debugging](screenshots/debugging_example.png)

During development, I ran into:
- Python environment issues in Kali Linux  
- API key configuration problems  
- Model compatibility errors  

These were resolved using virtual environments and proper API setup.

---

## 🧾 Sample Logic (Severity Scoring)

```python
def calculate_severity(alert):
    if alert["attempts"] >= 20:
        return "High"
    elif alert["attempts"] >= 10:
        return "Medium"
    return "Low"
```

---

## 🚀 How to Run

```bash
git clone https://github.com/YOUR_USERNAME/mini-ai-soc.git
cd mini-ai-soc

python3 -m venv venv
source venv/bin/activate

pip install google-genai

export GEMINI_API_KEY="your_api_key_here"

python soc_analyzer.py alerts.json
```

---

## 🔧 Troubleshooting

### Kali Python Error (externally-managed-environment)

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### API Key Issues

```bash
export GEMINI_API_KEY="your_api_key_here"
```

---

### Model / API Errors

- Verify model name (e.g., `gemini-3-flash-preview`)
- Check API quota limits (free tier can be restrictive)

---

## 🔐 Security Perspective

This project reflects how modern SOC teams:

- Prioritize alerts using structured logic  
- Enrich investigations with contextual data  
- Use AI to accelerate — not replace — analysis  
- Correlate multiple signals into a broader picture  

---

## 🚧 Future Improvements

- Integrate with SIEM tools (Splunk / ELK)  
- Pull live MITRE ATT&CK data  
- Add real-time log ingestion  
- Implement automated SOAR playbooks  
- Build a dashboard for visualization  

---

## 💡 Lessons Learned

- AI is most effective when paired with structured logic  
- Context (timeline, source, behavior) is critical  
- Debugging environments is part of real security work  
- Even low-severity alerts can matter in aggregate  

---

## 👤 Author

Shannon Smith  
Cybersecurity | Threat Detection | Incident Response | Automation & AI
