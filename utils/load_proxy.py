def load_proxy():
    with open('../proxy.txt', 'r') as f:
        proxies = f.read().splitlines()
        return proxies