from tools.news import *

def is_valid_url(url):
    return url.startswith("http://") or url.startswith("https://")

def format_article_section(item):
    headline = item.get("headlines", "").strip()
    summary = item.get("fullNews", "").strip()
    url = item.get("newsURL", "").strip()
    
    if is_valid_url(url):
        article_line = f"Full article: [Article]({url})"
    else:
        article_line = "Full article: Article not found."
    
    return f"## {headline}\nSummary: {summary}\n{article_line}\n"

def generate_malware_report():
    report = "# Report on malware news\n"
    for item in malware():
        report += format_article_section(item)
    return report

def generate_databreach_report():
    report = "# Report on data breach news\n"
    for item in data_breach():
        report += format_article_section(item)
    return report

def generate_cyber_attack_report():
    report = "# Report on cyber attack news\n"
    for item in cyber_attack():
        report += format_article_section(item)
    return report

def generate_vulnerability_report():
    report = "# Report on vulnerability news\n"
    for item in vulnerability():
        report += format_article_section(item)
    return report

