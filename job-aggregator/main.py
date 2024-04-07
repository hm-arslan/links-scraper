import scrapy

class JobSpider(scrapy.Spider):
    name = 'job_spider'

    def start_requests(self):
        # Replace 'your_url_here' with the URL of the job listings page
        url = 'your_url_here'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        job_listings = response.css('td.resultContent')
        for listing in job_listings:
            yield {
                'title': listing.css('h2.jobTitle a::text').get(),
                'company': listing.css('span.css-92r8pb::text').get(),
                'location': listing.css('div.css-1p0sjhy::text').get(),
                'job_type': listing.css('div.css-1cvo3fd::text').get()
            }

# Run the spider
# scrapy runspider job_spider.py -o jobs.csv
