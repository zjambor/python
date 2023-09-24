import time
from Workers.WikiWorker import WikiWorker
from Workers.YahooFinanceWorkers import YahooFinanceWorker

def main():
    scraper_start_time = time.time()

    wikiWorker = WikiWorker()
    current_workers = []

    for symbol in wikiWorker.get_sp_500_companies():
        yahooFinancePriceWorker = YahooFinanceWorker(symbol=symbol)
        current_workers.append(yahooFinancePriceWorker)

    for thr in current_workers:
        thr.join()

    print("Extracting time took:", round(time.time() - scraper_start_time, 1), "s")

if __name__ == "__main__":
    main()
