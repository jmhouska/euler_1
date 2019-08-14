def main (*args):
    max = args[0] if len(args) > 0 else 1000
    sum = 0
    for x in range(0, max):
       sum = sum + x if x % 3 == 0 or x % 5 == 0 else sum
    print(sum)
    return sum

if __name__ == "__main__":
    if main(10) != 23:
        print("Wrong...")
    main()