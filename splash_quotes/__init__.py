from scrapy.crawler import CrawlerProcess

from splash_quotes.spiders.scrolling import ScrollingSpider


def main():
    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "quotes.json": {"format": "json"},
            },
        }
    )

    process.crawl(ScrollingSpider)
    process.start()


if __name__ == "__main__":
    main()
