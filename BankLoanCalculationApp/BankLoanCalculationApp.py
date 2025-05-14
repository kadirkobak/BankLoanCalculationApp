def kredi_hesapla(kredi_tutari, faiz_orani, vade):
    
    aylik_faiz_orani = faiz_orani / 100 / 12

    
    if aylik_faiz_orani == 0:
        aylik_taksit = kredi_tutari / vade
    else:
        aylik_taksit = kredi_tutari * (aylik_faiz_orani * (1 + aylik_faiz_orani) ** vade) / ((1 + aylik_faiz_orani) ** vade - 1)

    toplam_geri_odeme = aylik_taksit * vade

    return aylik_taksit, toplam_geri_odeme


try:
    kredi_tutari = float(input("Kredi tutarını girin (TL): "))
    faiz_orani = float(input("Yıllık faiz oranını girin (%): "))
    vade = int(input("Vade süresini girin (ay): "))

    aylik_taksit, toplam_geri_odeme = kredi_hesapla(kredi_tutari, faiz_orani, vade)

    print(f"\nAylık taksit tutarı: {aylik_taksit:.2f} TL")
    print(f"Toplam geri ödeme: {toplam_geri_odeme:.2f} TL")

except ValueError:
    print("Lütfen geçerli bir sayı giriniz.")

