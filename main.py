from aims.dvd import DigitalVideoDisc
from aims.cart import Cart


def main():
    cart = Cart()
    cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", 19.95))
    cart.add_dvd(DigitalVideoDisc("Star Wars", "Science Fiction", 24.95))
    cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", 18.99))

    cart.print_cart()
    print(f"Total cost: {cart.total_cost()} $")


if __name__ == "__main__":
    main()
