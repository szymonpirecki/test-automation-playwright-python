class ProductModel:
    def __init__(self, title: str, price: float, description: str) -> None:
        self.title = title
        self.price = price
        self.description = description

    def __repr__(self) -> str:
        return f"ProductModel(title={self.title}, price={self.price}, description={self.description})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ProductModel):
            return NotImplemented
        return (
            self.title == other.title and
            self.price == other.price and
            self.description == other.description
        )
