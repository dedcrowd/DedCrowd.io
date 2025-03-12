import aiohttp
import asyncio
import time
from tqdm import tqdm  # Progress bar için

# Hedef URL
URL = "https://camo.githubusercontent.com/c15383d918954263b0a5402f934d84c859cea28f1f64ded6ba5d2fe0076e9631/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d64656463726f7764266c6162656c3d50726f66696c65253230766965777326636f6c6f723d306537356236267374796c653d666c6174"

# Konfigürasyon
MAX_CONCURRENT_REQUESTS = 360  # Aynı anda kaç istek yollanacak
TOTAL_REQUESTS = 1911651316  # Toplam kaç istek yollanacak

# Sayaçlar
completed_requests = 0
start_time = time.time()

# Progress Bar
progress_bar = tqdm(total=TOTAL_REQUESTS, desc="📡 İstek Gönderiliyor", unit="req")

# Asenkron İstek Gönderme Fonksiyonu
async def send_request(session):
    global completed_requests
    try:
        async with session.get(URL) as response:
            await response.text()
            completed_requests += 1
            progress_bar.update(1)  # Progress barı güncelle
    except Exception as e:
        print(f"❌ Hata: {e}")

# Ana Asenkron Döngü
async def main():
    global start_time
    start_time = time.time()
    
    connector = aiohttp.TCPConnector(limit_per_host=MAX_CONCURRENT_REQUESTS)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [send_request(session) for _ in range(TOTAL_REQUESTS)]
        await asyncio.gather(*tasks)  # Tüm istekleri paralel olarak başlat
    
    # Sonuçları Yazdır
    end_time = time.time()
    elapsed_time = end_time - start_time
    rps = TOTAL_REQUESTS / elapsed_time

    print("\n✅ **Test Tamamlandı!**")
    print(f"🕒 Geçen Süre: {elapsed_time:.2f} saniye")
    print(f"⚡ Ortalama Hız: {rps:.2f} istek/saniye")
    print(f"🎯 Toplam Gönderilen İstek: {completed_requests}")

# Çalıştır
asyncio.run(main())
progress_bar.close()

