import random
# id generator


def generateID(f, l):
        gen = random.randint(000000, 999999)
        rand_gen = f[0] + l[0] + "-" + str(gen)
        print(rand_gen)

        
firstname = input("Enter firstname: ")
lastname = input("Enter lastname: ")
generateID(firstname, lastname)
