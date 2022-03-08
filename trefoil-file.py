from topoly import alexander

def main():
    kp = alexander("trefoil.xyz", closure=0)
    print(str(kp))

if __name__ == "__main__":
    main()


