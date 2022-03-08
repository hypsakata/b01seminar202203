from topoly import alexander

def main():
    data = [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [-1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0]
            ]

    kp = alexander(data, closure=0)
    print(str(kp))

if __name__ == "__main__":
    main()


