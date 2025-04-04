class Converter:
    def __init__(self, kg):
        if not (type(kg) is int or type(kg) is float):
            raise ValueError("Килограммы")
        self.kg = kg

    def kq(self):
        return round(self.kg * 2.20462, 3)


fut = [12, 41]

for f1 in fut:
    converter = Converter(f1)
    print(f"{f1} кг => {converter.kq()} фунтов")
