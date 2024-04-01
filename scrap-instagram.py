# // Please use this script specifically for learning.
# // If you misuse it, it is your right.
# // I am not responsible for your detrimental actionsimport requests
import os
import random
import json
import time
from rich import print as prints
from bs4 import BeautifulSoup
from rich.panel import Panel as Panel
from rich.tree import Tree
from rich.table import Table as lipat
from rich.console import Console as solsapatu
from rich.columns import Columns as coli , Columns

console = solsapatu()
ugen = []
Agus = []
# ------ [ warna dasar ] ------ #
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m' # WARNA MATI
H = "\033[0;92m" # HIJAU
K = "\033[0;93m" #KUNING
M = '\x1b[1;91m' # MERAH
P = "\033[0m" # PUTIH

#------------------[ WARNA FOR RICH ]-------------------#
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

#------------------[ RANDOM COLOR RICH ]-------------------#
L1 = "[#875f5f]" # LIGHT
G1  = "[#ffd700]" # GOLD
M1  = "[#875fd7]" # MEDIUM GREEN
P1   = "[#FF00FF]" # PINK
W1  = "[#FFFFFF]" # WHITE
S1   = "[#87afff]" # SKY BLUE
O1   = "[#d78700]" # ORANGE3
O3   = "[#ff5fff]" # MEDIUM ORCH3


for x in range(1000):
    rr = random.randint
    rc = random.choice
    uacrack1 = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX2101 Build/RKQ1.{str(rr(111111,211111))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,99))} Mobile Safari/537.36"
    uacrack2 = f"Mozilla/5.0 (Linux; Android 11; Infinix X6512 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5000,5500))}.{str(rr(75,99))} Mobile Safari/537.36"
    uacrack3 = f"Mozilla/5.0 (Linux; Android {str(rr(9,13))}; LG-H918 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.{str(rr(3200,3500))}.84 Mobile Safari/537.36"
    uacrack4 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(9,16))}_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1"
    uacrack5 = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Redmi Note 9 Pro Max) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    uacrack6 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; LEGEND MAX Build/RP1A.{str(rr(111111,210000))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3500,4000))}.{str(rr(75,150))} UCBrowser/{str(rr(10,20))}.4.0.{str(rr(1300,1500))} Mobile Safari/537.36"
    uacrack7 = f"Mozilla/5.0 (Linux; Android 12; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,99))}.0.{str(rr(4500,4900))}.{str(rr(75,99))} Mobile Safari/537.36"
    uanyancek= random.choice([uacrack1, uacrack2, uacrack3, uacrack4, uacrack5, uacrack6, uacrack7])
    ugen.append(uanyancek)

def namapw():
    print('')
    idf = input(f"+_ masukan username : ")
    pas = input(f"+_ masukan password : ")
    time.sleep(1)
    ts = {{int(time.time())}}
    p = session.get("https://www.instagram.com/accounts/login/")
    heade = {
        'Host': 'www.instagram.com',
        'X-IG-App-ID': '1217981644879628',
        'X-IG-WWW-Claim': '0',
        'sec-ch-ua-mobile': '?1',
        'X-Instagram-AJAX': 'e776ba0cb975',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'X-ASBD-ID': '198387',
        'User-Agent': UA1,
        'X-CSRFToken': p.cookies['csrftoken'],
        'Origin': 'https://z-p42.www.instagram.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://z-p42.www.instagram.com/accounts/onetap/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    data = {
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pas}",
        "username": idf,
        "queryParams": "{}",
        "optIntoOneTap": 'false',
        "stopDeletionNonce": "",
        "trustedDeviceRecords": "{}"
    }
    response = session.post("https://www.instagram.com/accounts/login/ajax",
                            headers=heade,
                            data=data).text
    if "userld" in response or "sessionid" in session.cookies.get_dict():
        koki = (";").join(
            [ku + "=" + asu for ku, asu in session.cookies.get_dict().items()])
        Meledak = Tree(Panel.fit(f"[bold green]Nama instagram : {idf}"))
        Meledak.add(Panel.fit(f"[bold green]password instagram : {pas}"))
        Meledak.add(Panel.fit(f"[bold green]Cookies instagram : {koki}"))
        prints(Meledak)
        time.sleep(2)
        open('cookie/IG.txt', 'w').write(koki)
        open('username/IG.txt', 'w').write(idf)
        cek()
    elif "checkpoint_required" in response:
        koki = (";").join([
            ku + "=" + asu for ku, asu in response.cookies.get_dict().items()
        ])
        Meledak = Tree(Panel.fit(f"[bold yellow]Nama instagram : {idf}"))
        Meledak.add(Panel.fit(f"[bold yellow]password instagram : {pas}"))
        Meledak.add(Panel.fit(f"[bold yellow]Cookies instagram : {koki}"))
        prints(Meledak)
        exit()
    else:
        prints(Panel.fit(f"[bold red]username dan password anda salah"))


def menu():
    os.system('cls')
    try:cek_data = requests.get("http://ip-api.com/json/").json
    except:cek_data = {'-'}
    try:Iplu = cek_data["query"]
    except:Iplu = {'-'}
    prints(Panel.fit(f"[bold red]Warning!!!!. [bold white]this script not give to people and Don't sell it illegally or legally",style="bold green"))
    Agus.append(Panel(f"[bold white]MENU SCRAPING INSTAGRAM   Created by : Meledak X Cik",style="bold green"))
    Agus.append(Panel(f"[bold white]ip adres : {Iplu}",style="bold green"))
    console.print(Columns(Agus))
    Meledak = f"[bold white]1\n2\n3\n4"
    Meledak2 = f"[bold white]Pencarian scraping melewati foto\nPencarian scraping melewati nama\nPencarian scraping melewati link post\nUpdate Tools"
    Meledak3 = f"[bold green]ON[bold white]\n[bold green]ON[bold white]\n[bold red]OFF[bold white]\n[bold red]Up[bold white]"
    Cik = lipat()
    Cik.add_column(f"[bold white]NO", justify="center")
    Cik.add_column(f"[bold white]MENU", justify="center", width=52)
    Cik.add_column(f"[bold white]STATUS", justify="center")
    Cik.add_row(Meledak, Meledak2, Meledak3)
    console.print(Cik, justify="left", style=f"bold green")
    i = input("Masukan Pilihan : ")
    if i == '1':
        url = input(f'Masukan link foto : ')
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        caption = soup.find('meta', property='og:description')['content']
        likes = soup.find('meta', property='og:see_also')
        comments = soup.find('meta', property='og:see_also')
        print(f"Caption: {caption}")
    elif i == '2':
        username = input("Masukkan nama pengguna (username) Instagram: ")
        url = f"https://www.instagram.com/{username}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        followers_tag = soup.find('meta',
                                  attrs={
                                      'property': 'og:description',
                                      'content': True
                                  })
        if followers_tag:
            followers_content = followers_tag['content']
            followers_count = followers_content.split(',')[0].split()[0]
            following_tag = soup.find('meta',
                                      attrs={
                                          'property': 'og:description',
                                          'content': True
                                      })
        if following_tag:
            following_content = following_tag['content']
            following_count = following_content.split(',')[1].split()[0]
        post_tag = soup.find('meta',
                             attrs={
                                 'property': 'og:description',
                                 'content': True
                             })
        if post_tag:
            post_content = post_tag['content']
            post_count = post_content.split(',')[2].split()[0]
        print(f"Akun @{username}")
        print(f"Jumlah Pengikut: {followers_count}")
        print(f"Jumlah yang Diikuti: {following_count}")
        print(f"Jumlah Postingan: {post_count}")
    elif i == '3':
        prints(
            Panel.fit(
                f"[bold white]Maaf menu Ini masih dalam tahap pengembangan",
                style="bold green"))
        time.sleep(1)
        menu()
    elif i == '4':
        prints(
            Panel.fit(
                f"[bold white]Maaf menu Ini masih dalam tahap pengembangan",
                style="bold green"))
        time.sleep(1)
        menu()
    else:
        print("Pilihan tidak ditemukan")


if __name__ == "__main__":
    menu()
    #namapw()
