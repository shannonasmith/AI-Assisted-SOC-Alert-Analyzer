# 🛡️ AI-Assisted SOC Alert Analyzer

## 📌 Overview

This project simulates how a Security Operations Center (SOC) processes alerts — not just detecting them, but **triaging, investigating, and deciding what to do next**.

It is designed to demonstrate how **AI can assist (not replace)** a SOC analyst by adding context, validating decisions, and accelerating investigations.

Rather than treating alerts as isolated events, this system analyzes multiple signals together to produce **meaningful, actionable insight**.

---

## 🎯 What This Project Demonstrates

- Realistic SOC alert triage workflow  
- Mapping activity to **MITRE ATT&CK techniques**  
- Combining **rule-based detection + AI-assisted enrichment**  
- Multi-alert correlation and situational awareness  
- Investigation, validation, and troubleshooting in a lab environment  

---

## 🧠 System Architecture

    Input:
      alerts.json

    Processing Pipeline:
      → Rule-Based Triage
          - Severity scoring
          - MITRE ATT&CK mapping
          - Confidence scoring

      → Recommended Actions

      → Simulated Response

      → Timeline Reconstruction

      → AI Enrichment
          - Context enrichment
          - Severity validation
          - Investigation expansion

      → Batch Correlation
          - Severity distribution
          - MITRE coverage
          - Source correlation

    Output:
      Structured SOC-style analysis + summary

---

## ⚙️ How It Works

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
    AI Enrichment / Validation
    ↓
    Batch Summary + Correlation

---

## 📂 Repository Structure

    AI-Assisted-SOC-Alert-Analyzer/
    │
    ├── soc_analyzer.py
    ├── alerts.json
    ├── analysis_results.txt
    ├── screenshots/
    └── README.md

---

## 📸 Project Walkthrough

### ⚙️ 1. Development Workflow

![Development Workflow](screenshots/ai_analysis_output.png)

Before running the analyzer, I validated the working directory and project files inside the Kali VM.

This step shows:

- Accessing the project script
- Confirming the file structure
- Verifying the virtual environment exists

This reflects a normal development workflow before executing security tooling.

---

### 🧪 2. Environment Setup

![Environment Setup](screenshots/development_workflow.png)

The project was built and tested inside a Python virtual environment in Kali Linux.

This setup included:

- Installing required Python packages
- Isolating dependencies
- Preparing the environment for repeatable testing

Using a virtual environment helped prevent package conflicts and made troubleshooting easier.

---

### 📊 3. Per-Alert SOC Analysis

Each alert is processed individually using rule-based logic before AI enrichment is attempted.

The analyzer performs:

- Severity scoring
- MITRE ATT&CK mapping
- Confidence scoring
- Response recommendation generation
- Timeline reconstruction

#### ALERT-001 — Brute Force Activity

![Alert 1](screenshots/alert_001_analysis.png)

This alert was classified as:

- **Severity:** Medium
- **MITRE ATT&CK:** T1110 — Brute Force
- **Confidence:** Moderate

The output recommends investigating source IP `192.168.1.45` and monitoring the `admin` account for repeated failed authentication attempts.

---

#### ALERT-002 — Network Service Discovery / Reconnaissance

![Alert 2](screenshots/alert_002_analysis.png)

This alert was classified as:

- **Severity:** High
- **MITRE ATT&CK:** T1046 — Network Service Discovery
- **Confidence:** High

The output recommends blocking source IP `10.0.0.88` and isolating the affected host due to clear reconnaissance behavior.

---

#### ALERT-003 — Low-Volume Authentication Activity

![Alert 3](screenshots/alert_003_analysis.png)

This alert was classified as:

- **Severity:** Low
- **MITRE ATT&CK:** T1078 — Valid Accounts (possible account access attempt)
- **Confidence:** Moderate

The output recommends logging and monitoring activity from `172.16.0.12` because the behavior may be benign or represent early-stage probing.

---

### 🤖 4. AI Enrichment Attempt

The analyzer was designed to send each alert to an AI model for additional context and validation after the rule-based phase completed.

In this run, the AI stage did not complete successfully because the API quota was exceeded.

This is visible in the alert screenshots above, where the rule-based triage succeeded, but AI enrichment returned:

- `429 RESOURCE_EXHAUSTED`
- quota exceeded for the configured model

This reflects a real-world engineering consideration in AI-assisted security workflows:

- the SOC logic should still provide useful output even when AI services are unavailable
- AI should enrich analysis, not be the only source of decision-making

---

### 📈 5. SOC Batch Summary

![SOC Batch Summary](screenshots/soc_batch_summary.png)

After all alerts were processed, the system generated a batch-level summary showing:

- Total alerts processed
- Severity distribution
- MITRE ATT&CK breakdown
- Source IP correlation
- Repeat offender detection

This reflects how analysts move from **single-alert review** to **broader situational awareness**.

---

### 🔍 6. Investigation & Validation

![Nmap Scan](screenshots/nmap_scan.png)

After identifying suspicious activity, additional validation was performed with Nmap against `192.168.1.45`.

The scan confirmed:

- the host was up
- TCP port `53` was open
- the service was identified as `domain`

This demonstrates a realistic workflow where alert analysis leads to follow-on investigation to validate exposure and gather supporting evidence.

---

### 🔧 7. Troubleshooting: AI Model Configuration Error

![Model Error](screenshots/soc_analyzer_output.png)

During testing, one execution failed because the configured model was not supported by the API version in use.

The error showed:

- `404 NOT_FOUND`
- model not found / not supported for `generateContent`

This is an example of troubleshooting an AI integration issue rather than a SOC alert itself.

---

### 🛠️ 8. Troubleshooting: Execution Error

![Execution Error](screenshots/debugging_example.png)

Another issue occurred when attempting to run a script filename that did not exist in the project directory.

The error showed:

- `can't open file`
- `No such file or directory`

This highlights a common but realistic part of lab development: validating filenames, paths, and execution context before troubleshooting deeper logic issues.

---

## 🧾 Sample Logic (Severity Scoring)

    def calculate_severity(alert):
        if alert["attempts"] >= 20:
            return "High"
        elif alert["attempts"] >= 10:
            return "Medium"
        return "Low"

---

## 🚀 How to Run

    git clone https://github.com/shannonasmith/AI-Assisted-SOC-Alert-Analyzer.git
    cd AI-Assisted-SOC-Alert-Analyzer

    python3 -m venv venv
    source venv/bin/activate

    pip install google-genai

    export GEMINI_API_KEY="your_api_key_here"

    python soc_analyzer.py alerts.json

---

## 🔧 Troubleshooting

### Virtual Environment Setup

    python3 -m venv venv
    source venv/bin/activate

### API Key Setup

    export GEMINI_API_KEY="your_api_key_here"

### Common AI Integration Issues

- Verify the configured model name is valid
- Check whether the model supports the API method being used
- Confirm API quota has not been exhausted
- Re-run using a supported model if a `404 NOT_FOUND` error occurs

### Common Execution Issues

- Confirm the script filename is correct
- Verify the working directory before running Python files
- Use `ls` to confirm files are present

---

## 🔐 Security Perspective

This project reflects how modern SOC teams:

- Prioritize alerts using structured logic
- Map activity to ATT&CK techniques for analyst context
- Use AI as an enhancement layer rather than a dependency
- Investigate suspicious activity with follow-on validation
- Continue operating even when automation components fail

---

## 🚧 Future Improvements

- Integrate with SIEM platforms such as Splunk or ELK
- Pull MITRE ATT&CK data dynamically instead of relying on static mappings
- Add real-time log ingestion
- Add retry logic / graceful fallback for AI quota failures
- Build a dashboard for visualization
- Extend correlation across a larger alert set

---

## 💡 Lessons Learned

- Rule-based triage provides a reliable baseline even when AI fails
- AI enrichment is useful, but it should not be the only analysis path
- Environment setup and troubleshooting are part of real security engineering work
- Investigation steps such as service validation improve confidence in alert interpretation
- Small execution and configuration issues can significantly affect a workflow if not handled carefully

---

## 👤 Author

Shannon Smith  
Cybersecurity | Threat Detection | Incident Response | Automation & AI
