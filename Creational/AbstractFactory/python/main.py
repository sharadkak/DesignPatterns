from interfaces import AbstractFactory
from factories import WinterClothes, SummerClothes


def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_bottoms()
    product_b = factory.create_tops()

    print(f"In BottomWear, Selling {product_a.__class__.__name__} from {product_a.brand_name} for {product_b.price()}")
    print(f"In TopWear,Selling {product_b.__class__.__name__} from {product_b.brand_name} for {product_b.price()}")


if __name__ == "__main__":
    print("Client: Display Winter clothes:")
    client_code(WinterClothes())

    print("\n")

    print("Client: Display summer clothes:")
    client_code(SummerClothes())