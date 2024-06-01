# Write a Python method in Oop called “calculate_area” that takes the radius of a circle as input and returns the area of the circle, write program using Oop.

class circle:
    def __init__(self,radius):
        self.circle_radius=radius
    
    def calculate_area(self):
        area=3.14*radius**2
        return area

radius = int(input("enter the radius: "))
obj = circle(radius)
area = obj.calculate_area()
print(f"the area of circle is {area}")

#Write a Python method in Oop called “calculate_discount” that calculates the final price of an item after applying a discount percentage. The function should take the original price and the discount percentage as inputs.

class cost:
    def __init__(self,original_price,discount):
        self.original_price=original_price
        self.discount=discount
    def calculate_discount(self):
        dis_ammount = self.discount/100 * self.original_price
        final_amount = self.original_price - dis_ammount
        return final_amount
original_price = int(input("enter the price: "))
discount = int(input("enter the discount: "))
obj = cost(original_price,discount)
Final_amount = obj.calculate_discount()
print(f"the final amount is {Final_amount}")

# Write a method in Oop named “count_vowels” that takes a string as input and returns the count of vowels (both uppercase and lowercase) in the string.

class alphabet:
    def __init__(self,text):
        self.text=text
    def count_vowel(self):
        vowels= "aeiouAEIOU"
        count=0
        for i in self.text:
            if i in vowels:
                count= count+1
        return count
text=input("enter the string: ")
obj = alphabet(text)
a = obj.count_vowel()
print(f"total vowels are {a} ")