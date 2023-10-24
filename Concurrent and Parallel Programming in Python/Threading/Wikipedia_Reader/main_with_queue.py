import time
from multiprocessing import Queue
from Workers.WikiWorker import WikiWorker
from Workers.YahooFinanceWorkers import YahooFinanceWorker

def main():
    symbol_queue = Queue()
    scraper_start_time = time.time()

    wikiWorker = WikiWorker()
    # current_workers = []

    for symbol in wikiWorker.get_sp_500_companies():
        symbol_queue.put(symbol)
        # yahooFinancePriceWorker = YahooFinanceWorker(symbol=symbol)
        # current_workers.append(yahooFinancePriceWorker)

    # for thr in current_workers:
    #     thr.join()

    print(symbol_queue)
    print(symbol_queue.get())
    print("Extracting time took:", round(time.time() - scraper_start_time, 1), "s")

if __name__ == "__main__":
    main()
