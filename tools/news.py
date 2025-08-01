from cybernews.cybernews import CyberNews

news = CyberNews()

def malware():
    return news.get_news("malware")

def data_breach():
    return news.get_news("dataBreach") 

def cyber_attack():
    return news.get_news("cyberAttack")

def vulnerability():
    return news.get_news("vulnerability")

