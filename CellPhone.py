import CellPhoneClass as cc


def main():
    m = input("Who is the manufacturer?: ")

    mod = input("What is the model?: ")

    rp = input("What is the retail price?: ")

    phone = cc.CellPhone(m, mod, rp)

    phone.set_manufact(m)
    phone.set_model(mod)
    phone.set_retail_price(rp)

    print("The manufacturer is: ", m)
    print("The model is: ", mod)
    print("The retail price is: ", rp)


main()