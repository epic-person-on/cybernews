from tools.markdown import *

def main():
    with open("reports/malware_report.md", "w") as f:
        f.write(generate_malware_report())

    with open("reports/data_breach_report.md", "w") as f:
        f.write(generate_databreach_report())

    with open("reports/cyber_attack_report.md", "w") as f:
        f.write(generate_cyber_attack_report())

    with open("reports/major_vulnerability_report.md", "w") as f:
        f.write(generate_vulnerability_report())
        
if __name__ == "__main__":
    main()
