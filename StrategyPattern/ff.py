class DiscountService:
    def calculate_discount(self, discount_type:str):
        if discount_type=="diwali":
            print("Apply diwali discount")

        elif discount_type=="first_order":
            print("Apply first order discount")

        else:
            print("No discount")