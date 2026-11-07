from aims import __version__
from aims.dvd import DigitalVideoDisc
from aims.cart import Cart
from aims.search import search_by_title


def main():
    print(f"AIMS-mini v{__version__}")

    cart = Cart()
    cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", 19.95))
    cart.add_dvd(DigitalVideoDisc("Star Wars", "Science Fiction", 24.95))
    cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", 18.99))

    cart.print_cart()

    print("Ket qua tim 'lion':")
    for dvd in search_by_title(cart.items, "lion"):
        print(f"  {dvd.title}")

    print(f"Total cost: {cart.total_cost()} $")


if __name__ == "__main__":
    main()
