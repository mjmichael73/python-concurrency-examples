from stock_thread import Stock


def main() -> None:
    symbols = ["MSFT", "GOOGL", "AAPL", "META"]

    threads = []

    for symbol in symbols:
        t = Stock(symbol)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
        print(t)


if __name__ == "__main__":
    main()
