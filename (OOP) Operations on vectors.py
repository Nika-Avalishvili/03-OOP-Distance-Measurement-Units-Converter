# 1. კლასით განისაზღვროს მათემატიკური ოპერაციების ქმედება ვექტორზე და ვიფრებზე
class VectorClass:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance (other, VectorClass):
            return VectorClass(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance (other,(int,float)):
            return VectorClass(self.x + other, self.y + other,self.z + other)

    def __sub__(self, other):
        if isinstance (other, VectorClass):
            return VectorClass(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance (other,(int,float)):
            return VectorClass(self.x - other, self.y - other,self.z - other)

    def __mul__(self, other):
        if isinstance (other, VectorClass):
            return VectorClass(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance (other,(int,float)):
            return VectorClass(self.x * other, self.y * other,self.z * other)

    def __truediv__(self, other):
        if isinstance (other, VectorClass):
            return VectorClass(self.x / other.x, self.y / other.y, self.z / other.z)
        elif isinstance (other,(int,float)):
            return VectorClass(self.x / other, self.y / other,self.z / other)

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

# 2. მომხმარებელმა მენიუში უნდა აირჩიოს ოპერაცია
user_choice = input('\nმოგესალმებით, \nთქვენ იმყოფებით მთავარ მენიუში. \nგთხოვთ, აირჩიოთ სასურველი ოპერაცია \n(მიმატება, გამოკლება, გამრავლება, გაყოფა): ')
correct_list= ["მიმატება", "გამოკლება", "გამრავლება", "გაყოფა"]

# 3. წინა სვლაზე შესაბამისი პუნქტის არჩევის შემდეგ პროგრამაში მოხდეს ვექტორების ან რიცხვების ინტერაქტიული შეტანა;
if user_choice in correct_list:
    vectors = []
    for i in range(2):
        first_vec = input("\nთუ შეგყავთ ვექტორი აკრიფეთ სიმბოლო Y, მხოლოდ ერთი ციფრის შეყვანის შემთხვევაში N: ").upper()
        if first_vec == "Y":
            x1 = float(input("შეიყვანეთ x კოორდინატი: "))
            y1 = float(input("შეიყვანეთ y კოორდინატი: "))
            z1 = float(input("შეიყვანეთ z კოორდინატი: "))
            vector1 = VectorClass(x1,y1,z1)
            vectors.append(vector1)
        else:
            vector1 = float(input("შეიყვანეთ ციფრი: "))
            vectors.append(vector1)

final_operation= {"მიმატება":vectors[0]+vectors[1], "გამოკლება":vectors[0]-vectors[1], "გამრავლება":vectors[0]*vectors[1], "გაყოფა":vectors[0]/vectors[1]}

print('\n')
print(f'თქვენს მიერ შეყვანილი მონაცემები შემდეგნაირად გამოიყურება: 1). {vectors[0]}, 2). {vectors[1]}')
print('\n')
print(f'მიღებული საბოლოო ვექტორია: {final_operation[user_choice]}',"\n")
