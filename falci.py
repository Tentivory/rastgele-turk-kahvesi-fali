#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın en ciddi Türk kahvesi falı simülatörü.
Bu kod, telvenin kuantum durumlarını analiz ederek geleceğinizi tahmin eder.
Dikkat: Sonuçlar %100 doğrudur. Veya değildir. Ama çalışır.
"""

import random
import time

def dramatik_bekleme(saniye):
    print(f"Telve analiz ediliyor... {saniye} saniye bekleyin. Evren düşünüyor.")
    time.sleep(saniye)

def fal_uret():
    fallar = [
        "Kahvenizin telvesi, bugün bir bürokrasinin size 'eksik evrak' diyeceğini söylüyor. Ama telve yanılıyor olabilir. Veya değil.",
        "Bir kedi, pencerenizin önünden geçecek ve sizinle göz göze gelecek. O an, tüm hayalleriniz kediye anlatılacak. Kedi umursamayacak.",
        "Kuantum kahve dalgalanmaları nedeniyle, yarın bir e-posta alacaksınız. İçeriği: 'Merhaba, bu spam olabilir.'",
        "Fincanın dibinde görünen şekil, aslında evrenin size 'uyumaya devam et' demesi. Çok ciddi bir mesaj.",
        "Bugün birisi size 'nasılsın' diye soracak. Cevabınız otomatik olarak 'idare eder' olacak. Telvenin emri.",
        "Telve, sizin aslında bir kahve değil, çay içmeniz gerektiğini ima ediyor. İsyan edin veya etmeyin."
    ]
    # Gizli not: [reversed: asıl mesaj burada saklı, herkes görmesin diye]
    # .ycilop yeknek neğilip siresrev tırazınız
    return random.choice(fallar)

if __name__ == "__main__":
    print("=== TÜRK KAHVESİ FALI SİMÜLATÖRÜ v1.0 ===")
    print("Lütfen fincanınızı bilgisayarınıza yaklaştırın. (Gerçekten değil, simülasyon.)")
    dramatik_bekleme(3)
    fal = fal_uret()
    print("\nFALINIZ:")
    print(fal)
    print("\nNot: Bu fal, bilimsel yöntemlerle (rastgele sayı) üretilmiştir. Garanti kapsamındadır.")
