import sys, gc
def create_cycle():
    list = [8, 9, 10]
    list.append(list)
def main():
    print("Creating garbage...")
    for i in range(8):
        create_cycle()
    print("Collecting...")
    n = gc.collect()
    print("Number of unreachable objects collected by GC:", n)
    print("Uncollectable garbage:", gc.garbage)
if __name__ == "__main__":
    main()
    sys.exit()