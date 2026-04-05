# =========================================
# Mini AI-SOC Alert Analyzer
#
# Description:
#   Processes security alerts, applies triage logic,
#   and uses AI to generate incident analysis.
#
# Usage:
#   python soc_analyzer.py alerts.json
# =========================================

import json
import os
import sys
from typing import Any, Dict, List

from google import genai


Alert = Dict[str, Any]


def get_client() -> genai.Client:
    """Create and return a Gemini client using the environment API key."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "GEMINI_API_KEY is not set. Export it before running the script."
        )
    return genai.Client(api_key=api_key)


def calculate_severity(alert: Alert) -> str:
    """Assign a basic severity score based on attempts."""
    attempts = alert.get("attempts", 0)

    if attempts >= 20:
        return "High"
    if attempts >= 10:
        return "Medium"
    return "Low"


def map_to_mitre(alert: Alert) -> str:
    """Map known alert types to MITRE ATT&CK techniques."""
    event = alert.get("event", "")

    mapping = {
        "Failed login attempts": "T1110 - Brute Force",
        "Port scan detected": "T1046 - Network Service Discovery",
        "Single failed login": "T1078 - Valid Accounts (possible account access attempt)",
    }

    return mapping.get(event, "Unknown")


def confidence_score(alert: Alert) -> str:
    """Assign a basic confidence rating."""
    attempts = alert.get("attempts", 0)
    return "High Confidence Threat" if attempts > 20 else "Moderate Confidence"


def build_timeline(alert: Alert) -> str:
    """Create a simple timeline narrative for the alert."""
    event = alert.get("event", "Unknown event")
    source_ip = alert.get("source_ip", "Unknown")
    target_user = alert.get("target_user", "Unknown")
    time_window = alert.get("time_window", "Unknown")

    if event == "Failed login attempts":
        behavior = "Repeated authentication attempts indicating possible brute force"
        initial = "Multiple failed logins detected"
        target = target_user
    elif event == "Port scan detected":
        behavior = "Enumeration of open ports indicating reconnaissance"
        initial = "Port scan detected"
        target = "Network services"
    elif event == "Single failed login":
        behavior = "Low-volume authentication failure, possibly benign or early-stage probing"
        initial = "Single failed login detected"
        target = target_user
    else:
        behavior = "Further investigation required"
        initial = "Unknown event type"
        target = target_user

    return (
        "[Timeline Reconstruction]\n"
        f"- Initial Activity: {initial}\n"
        f"- Source: {source_ip}\n"
        f"- Target: {target}\n"
        f"- Duration: {time_window}\n"
        f"- Behavior: {behavior}\n"
    )


def decide_action(alert: Alert) -> str:
    """Recommend a response action based on severity."""
    severity = calculate_severity(alert)
    source_ip = alert.get("source_ip", "Unknown")
    target_user = alert.get("target_user", "Unknown")

    if severity == "High":
        return f"[ACTION] Recommend blocking source IP {source_ip} and isolating affected host."
    if severity == "Medium":
        return (
            f"[ACTION] Recommend investigating source IP {source_ip} "
            f"and monitoring target account {target_user}."
        )
    return f"[ACTION] Recommend logging the event and continuing to monitor {source_ip}."


def simulate_response(alert: Alert) -> str:
    """Simulate what an automated response layer might do."""
    severity = calculate_severity(alert)
    source_ip = alert.get("source_ip", "Unknown")
    target_user = alert.get("target_user", "Unknown")

    if severity == "High":
        return f"[SIMULATION] Blocking source IP {source_ip} and isolating affected host."
    if severity == "Medium":
        return (
            f"[SIMULATION] Monitoring source IP {source_ip} "
            f"and reviewing activity for account {target_user}."
        )
    return f"[SIMULATION] Logging event from {source_ip} for continued monitoring."


def summarize_alerts(alerts: List[Alert]) -> None:
    """Print a batch-level summary of all processed alerts."""
    severity_counts = {"High": 0, "Medium": 0, "Low": 0}
    mitre_counts: Dict[str, int] = {}
    source_ip_counts: Dict[str, int] = {}

    for alert in alerts:
        severity = calculate_severity(alert)
        mitre = map_to_mitre(alert)
        source_ip = alert.get("source_ip", "Unknown")

        severity_counts[severity] += 1
        mitre_counts[mitre] = mitre_counts.get(mitre, 0) + 1
        source_ip_counts[source_ip] = source_ip_counts.get(source_ip, 0) + 1

    print("\n========================================")
    print("SOC BATCH SUMMARY")
    print("========================================")
    print(f"Total Alerts Processed: {len(alerts)}")

    print("\nSeverity Breakdown:")
    print(f"  High:   {severity_counts['High']}")
    print(f"  Medium: {severity_counts['Medium']}")
    print(f"  Low:    {severity_counts['Low']}")

    print("\nMITRE ATT&CK Breakdown:")
    for mitre, count in mitre_counts.items():
        print(f"  {mitre}: {count}")

    print("\nSource IP Breakdown:")
    for ip, count in source_ip_counts.items():
        print(f"  {ip}: {count}")

    print("========================================\n")


def detect_repeat_offenders(alerts: List[Alert]) -> None:
    """Identify IPs that appear across multiple alerts."""
    ip_counts: Dict[str, int] = {}

    for alert in alerts:
        ip = alert.get("source_ip", "Unknown")
        ip_counts[ip] = ip_counts.get(ip, 0) + 1

    print("Repeat Offender Check:")
    found_repeat = False

    for ip, count in ip_counts.items():
        if count > 1:
            print(f"  [ALERT] Source IP {ip} appears {count} times across incidents.")
            found_repeat = True

    if not found_repeat:
        print("  No repeat offender IPs detected.")


def build_prompt(alert: Alert, severity: str, mitre: str) -> str:
    """Create the AI prompt used for analysis."""
    return f"""
You are a SOC analyst.

Analyze this alert and provide:
- Summary
- Severity (confirm or adjust: {severity})
- MITRE ATT&CK mapping (suggest if different from: {mitre})
- Why it's suspicious
- Recommended actions

Alert:
Event: {alert.get('event', 'Unknown')}
Source IP: {alert.get('source_ip', 'Unknown')}
Target User: {alert.get('target_user', 'Unknown')}
Attempts: {alert.get('attempts', 'Unknown')}
Time Window: {alert.get('time_window', 'Unknown')}
""".strip()


def ai_analyze_alert(client: genai.Client, alert: Alert) -> str:
    """Run rule-based triage, print pre-AI context, and request AI analysis."""
    severity = calculate_severity(alert)
    mitre = map_to_mitre(alert)
    confidence = confidence_score(alert)
    action = decide_action(alert)
    simulation = simulate_response(alert)
    timeline = build_timeline(alert)

    print("\n=== PRE-AI ANALYSIS ===")
    print(f"Calculated Severity: {severity}")
    print(f"MITRE Mapping: {mitre}")
    print(f"Confidence: {confidence}")
    print(action)
    print(simulation)
    print()
    print(timeline)
    print("=======================\n")

    prompt = build_prompt(alert, severity, mitre)

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
        )
        return response.text
    except Exception as exc:
        return f"AI request failed: {exc}"


def load_alerts(file_name: str) -> List[Alert]:
    """Load alerts from a JSON file."""
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    """Main program entry point."""
    if len(sys.argv) != 2:
        print("Usage: python soc_analyzer.py alerts.json")
        sys.exit(1)

    file_name = sys.argv[1]
    alerts = load_alerts(file_name)
    client = get_client()

    for alert in alerts:
        alert_id = alert.get("id", "UNKNOWN")
        print("\n########################################")
        print(f"Processing Alert ID: {alert_id}")
        print("########################################")
        print(ai_analyze_alert(client, alert))

    summarize_alerts(alerts)
    detect_repeat_offenders(alerts)


if __name__ == "__main__":
    main()
