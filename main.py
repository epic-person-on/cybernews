from tools.markdown import *

def main():
    with open("reports/malware.md", "w") as f:
        f.write(generate_malware_report())
    with open("reports/data_breach.md", "w") as f:
        f.write(generate_databreach_report())
    

if __name__ == "__main__":
    main()
