import requests
from bs4 import BeautifulSoup
from threading import Thread
import urllib3
from urllib3.exceptions import InsecureRequestWarning

# 记得改成自己的代理的地址
proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}

results_ok = []
results_others = []

def request(line):
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    }
    data = {
        'prompt': 'hi',
        'options': {},
        'systemMessage': 'You are ChatGPT, a large language model trained by OpenAI. Follow the user\'s instructions carefully. Respond using markdown.',
        'temperature': 0.8,
        'top_p': 1
    }
    url = f'{line}/api/chat-process'
    
    try:
        with requests.Session() as session:
            # 发起 GET 请求，获取网站title
            get_response = session.get(line, headers=headers, verify=False, timeout=10, proxies=proxies)
            
            # 发起 POST 请求，测试网站是否能正常聊天
            response = session.post(url=url, json=data, headers=headers, verify=False, timeout=10, proxies=proxies)
        
        soup = BeautifulSoup(get_response.text, 'html.parser')
        title = soup.title.string
        
        if response.status_code == 200:
            if 'error' not in response.text and 'fail' not in response.text and title == 'ChatGPT Web':
                print(line)
                results_ok.append(line)
            elif 'gpt' in title:
                print(f'{url} {title}')
                results_others.append(line)
    
    except Exception as e:
        pass


if __name__ == '__main__':
    urllib3.disable_warnings(InsecureRequestWarning)
    
    # 从用户输入中获取 ChatGPT URL 文档路径
    filepath = input('输入gpt文档：')
    
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

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
        f.write('\n\n-----others-----\n')
        for result in results_others:
            f.write(result + '\n')
