import requests
from threading import Thread
import urllib3
from urllib3.exceptions import InsecureRequestWarning

# 记得改成自己的代理的地址
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

results_ok = set()

def extract_domain(line):
    # 移除链接尾部的斜杠
    line = line.rstrip('/')
    
    # 提取域名部分
    start_index = line.find("//")
    end_index = line.find("/", start_index + 2)
    
    return line[:end_index] if end_index != -1 else line


def request(line):
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    }
    data = {"prompt": "Help me calculate the md5 value of admin", "options": {}}
    
    domain = extract_domain(line)
    url = f'{domain}/api/chat-process'
    
    try:        
        # 发起 POST 请求，测试网站是否能正常聊天, proxies=proxies
        response = requests.post(url=url, json=data, headers=headers, verify=False, timeout=10)
        
        if "21232f297a57a5a743894a0e4a801fc3" in response.text:
            print(line)
            results_ok.add(domain)
    
    except requests.RequestException as e:
        # print(e)
        pass

if __name__ == '__main__':
    urllib3.disable_warnings(InsecureRequestWarning)
    
    # 从用户输入中获取 ChatGPT URL 文档路径
    filepath = input('输入gpt文档：')
    
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    # for line in lines:
    #     print(line)

    threads = []
    for line in lines:
        t = Thread(target=request, args=(line,))
        threads.append(t)

    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

    with open('output.txt', 'w') as f:
        for result in results_ok:
            f.write(result + '\n')
