
def pythonFirst(num):
    for x in range(num):
        print("Hello Python ", x, " times!\n")



def main():
    num = int(input("Enter a number:"))
    print("\n")
    pythonFirst(num)

if __name__ == "__main__":
    main()