while True:
    print(" =================================================")
    h = float(input("Vui long nhap chieu cao cua ban : "))
    w = float(input("Vui long nhap can nang cua ban : "))
    m = h / 100
    BMI = w/( (h/100) **2)
    if  BMI < 16 :
        print("Ban dang thieu can nang !")
    elif BMI <= 18.5:
        print("Ban can giam can !")
    elif BMI <= 25:
        print("Ban can doi ^^")
    elif BMI<= 30:
        print("Ban dang thua can ! ")
    else:
        print("Ban beo phi` cmnr =))))")
        
