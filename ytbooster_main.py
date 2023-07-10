import ytbooster

TIMES_TO_RUN = 1000

def main() -> None:
    for _ in range(TIMES_TO_RUN):
        ytbooster.run_ytbooster()

if __name__ == "__main__":
    main()