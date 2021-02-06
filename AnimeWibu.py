import os, json, requests, sys

logo = """
> INI ADALAH SCRIP MENCARI PERCAKAPAN ANIME SECARA RANDOM
> OPEN  SOURCE CODE YA TOD LUMAYAN TAMBAH ILMU:v
━━━━━ ━━━━━ ━━━━━ ━━━━━ ━━━━━ ━━━━━━━━━━ ━━━━━ ━━━━━ ━━━━━
SCRIP RANDOM CHAT ALL ANIME
━━━━━ ━━━━━ ━━━━━ ━━━━━ ━━━━━ ━━━━━
CREATOR BY : <\>MANDO-XPLOIT
WHATSAPP ME: 085361524681
https://github.com/MRKALIT09
TEAM CYBER : MEDAN-XPLOITER
━━━━━ ━━━━━ ━━━━━ ━━━━━ ━━━━━ ━━━━━
"""

url='https://lolhuman.herokuapp.com/api/random/quotesnime'

req=lambda web: requests.get(web)

def main():
    os.system('clear')
    print(logo)
    http=req(url)
    jeson=json.loads(http.text)
    data=jeson['result']
    print('anime          :'+data['anime'])
    print('episode        :'+data['episode'])
    print('character      :'+data['character'])
    print('Quote          :'+data['quote'])
    ulang=input('Mau Search Lagi ? ?Y/N : ')
    if ulang == "Y" :
        main()
    else:
        sys.exit()

if __name__=='__main__' :
    os.system('clear')
    print(logo)
    cari=input('Mau Cari Percakapan Lagi? (Y/N) : ')
    if cari == "Y":
        main()
    else:
        sys.exit()

