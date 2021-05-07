# adet tam sayi girilip bu tam sayilarin asalligi kontrol edilecek

sayi_listesi = []
for i in range(0,5):
    sayi = int(input("Lutfen bir sayi giriniz: "))
    sayi_listesi.append(sayi)
    
    if sayi > 1:
        for s in range(2,sayi):
            if (sayi % s) == 0:
                print("Sayi asal sayi DEGILDIR.")
                break
        else:
                print("Sayi asal sayidir")
        
    else:
        print("Sayi Asal sayi DEGILDIR.")
  

     





    
     

    

        