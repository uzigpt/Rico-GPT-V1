print("Not: Bu RicoGPT'yi Kodlamak İçin Baya Bi Uğraştım Emeğimin Karşılığında Bu Kodu Kullanıp GPT açarsanız ve Bu Kod Uzinin Kodudur diye etiket atın Eğer Bu Kodları Düzenliyip Çalıp Benim Diyenlere Telif Atılacaktır")
import time
import sys
import random
import asyncio

async def print_ascii_art():
    art = r"""   __ _             ___   ___  _____ 
  /__(_) ___ ___   / _ \ / _ \/__   \
 / \// |/ __/ _ \ / /_\// /_)/  / /\/
/ _  \ | (_| (_) / /_\\/ ___/  / /   
\/ \_/_|\___\___/\____/\/      \/    
                                     
   ___              _____  _____     
  / __\/\_/\  /\ /\/ _  /  \_   \    
 /__\//\_ _/ / / \ \// /    / /\/    
/ \/  \ / \  \ \_/ // //\/\/ /_      
\_____/ \_/   \___//____/\____/      
                                     """
    print(art)

async def simulate_progress():
    for i in range(101):
        await asyncio.sleep(random.uniform(0.05, 0.1))
        sys.stdout.write(f"\rBağlantı İlerliyor... % {i}%")
        sys.stdout.flush()

async def ping_test():
    ping_times = ["20ms", "35ms", "50ms", "100ms", "200ms"]
    print("\nPing testi başlatılıyor...")
    for _ in range(3):
        await asyncio.sleep(1)
        ping = random.choice(ping_times)
        print(f"Ping: {ping}")
    print("\nPing testi tamamlandı!")

async def connect_to_uzi_ai():
    await print_ascii_art()
    print("UziAI'ye bağlanıyor...\n")
    await simulate_progress()
    await ping_test()
    print("\n✔ BAĞLANILDI!\n")