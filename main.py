class Calculator:
    def __init__(self):
        pass

    def son_kirit(self):
        while True:
            try:
                son = float(input("Sonni kiriting: "))
                return son
            except ValueError:
                print("Iltimos, son kiritishingiz kerak.")

    def tozalash(self, son):
        return son.replace(" ", "")

    def ertalash(self, son):
        return float(self.tozalash(son))

    def qoshish(self, son1, son2):
        return son1 + son2

    def ayirish(self, son1, son2):
        return son1 - son2

    def ko'paytirish(self, son1, son2):
        return son1 * son2

    def bo'lish(self, son1, son2):
        if son2 != 0:
            return son1 / son2
        else:
            return "Bo'lishga bo'linmaning 0 ga teng bo'lishi mumkin emas."

    def ishlatish(self):
        while True:
            print("\nCalculator CLI")
            print("1. Qo'shish")
            print("2. Ayirish")
            print("3. Ko'paytirish")
            print("4. Bo'lish")
            print("5. Chiqish")
            tanlov = input("Tanlovni kiriting: ")
            if tanlov == "5":
                break
            elif tanlov not in ["1", "2", "3", "4"]:
                print("Iltimos, to'g'ri tanlov kiriting.")
                continue
            son1 = self.son_kirit()
            son2 = self.son_kirit()
            if tanlov == "1":
                print(f"{son1} + {son2} = {self.qoshish(son1, son2)}")
            elif tanlov == "2":
                print(f"{son1} - {son2} = {self.ayirish(son1, son2)}")
            elif tanlov == "3":
                print(f"{son1} * {son2} = {self.ko'paytirish(son1, son2)}")
            elif tanlov == "4":
                print(f"{son1} / {son2} = {self.bo'lish(son1, son2)}")

calculator = Calculator()
calculator.ishlatish()
