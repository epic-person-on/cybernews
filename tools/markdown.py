from tools.news import *

def generate_malware_report():
    report = "# Report on malware news\n"
    section = ""
    data = malware()
    for item in data:
        section = f"## {item.get("headlines", "").strip()} \n Summary: {item.get("fullNews", "").strip()} \n Full article: [Article]({item.get("newsURL", "")}) \n"
        report += section
        section = ""
    return report

def generate_databreach_report():
    report = "# Report on data breach news\n"
    section = ""
    data = data_breach()
    for item in data:
        section = f"## {item.get("headlines", "").strip()} \n Summary: {item.get("fullNews", "").strip()} \n Full article: [Article]({item.get("newsURL", "")}) \n"
        report += section
        section = ""
    return report

def generate_cyber_attack_report():
    report = "# Report on cyber attack news\n"
    section = ""
    data = cyber_attack()
    for item in data:
        section = f"## {item.get("headlines", "").strip()} \n Summary: {item.get("fullNews", "").strip()} \n Full article: [Article]({item.get("newsURL", "")}) \n"
        report += section
        section = ""
    return report

def generate_vulnerability_report():
    report = "# Report on vulnerability news\n"
    section = ""
    data = vulnerability()
    for item in data:
        section = f"## {item.get("headlines", "").strip()} \n Summary: {item.get("fullNews", "").strip()} \n Full article: [Article]({item.get("newsURL", "")}) \n"
        report += section
        section = ""
    return report

def generate_security_report():
    report = "# Report on cyber security news\n"
    section = ""
    data = security()
    for item in data:
        section = f"## {item.get("headlines", "").strip()} \n Summary: {item.get("fullNews", "").strip()} \n Full article: [Article]({item.get("newsURL", "")}) \n"
        report += section
        section = ""
    return report




