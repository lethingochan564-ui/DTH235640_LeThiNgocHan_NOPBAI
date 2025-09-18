def oscillate(start, count):
    for k in range(start, count):
        yield k
        yield -k
def main():
    print(list(oscillate(-3, 5)))
    for n in oscillate(-3, 5):
        print(n, end=' ')
    print()
if __name__ == "__main__":
    main()