import scrapy
#from selenium import webdriver
from scrapy_selenium import SeleniumRequest


class AgentSpider(scrapy.Spider):
    name = "agent"
    #allowed_domains = ["www.homes.com"]
    #start_urls = ["https://www.homes.com/homes-for-sale/?sk=B22JVNmFQtm9JMn9L0BNhwPfNO-zb0kJIu_233mCmQg&bb=z0o3w_87uO3z-zw13a"]

    def start_requests(self):
        yield SeleniumRequest(
            url = "https://www.homes.com/homes-for-sale/?sk=B22JVNmFQtm9JMn9L0BNhwPfNO-zb0kJIu_233mCmQg&bb=z0o3w_87uO3z-zw13a",
            wait_time = 5,
            callback = self.parse
        )
        

    def parse(self, response):
        houses = response.xpath("//ul[@class='placards-list']/li")
        print(len(houses))
        for hous in houses:
            agency_name = hous.xpath(".//span[@class='agency-name']/text()").get()
            relative_link = hous.xpath(".//div[@class='for-sale-content-container']/a/@href").get()
            absolute_url = response.urljoin(relative_link)
            yield response.follow(url=absolute_url, callback=self.parse_agents, cb_kwargs={'agency_name':agency_name,'absolute_url': absolute_url})

    def parse_agents(self, response,agency_name, absolute_url):
        price = response.xpath("//span[@id='price']/text()").get()
        address = response.xpath("normalize-space(//h1[@class='property-info-address-main']/text())").get()
        city = response.xpath("(//a[@class='standard-link text-only']/text())[1]").get()
        agent = response.xpath("normalize-space((//a[@class='agent-information agent-information-fullname standard-link text-only']/text())[1])").get()
        phone = response.xpath("(//a[@class='agent-information agent-information-phone-number standard-link text-only']/text())[1]").get()
        email = response.xpath("(//span[@class='agent-information agent-information-email']/text())[1]").get()
        

            # Split the agent's name into first name and last name
        if agent:
            name_parts = agent.split()
            if len(name_parts) == 2:
                first_name, last_name = name_parts
            else:
                first_name = name_parts[0]
                last_name = None
        else:
            first_name = None
            last_name = None
        
        yield{
            'agency_name':agency_name,
            'listing_link': absolute_url,
            'first_name': first_name,
            'last_name': last_name,
            'listing_agent':agent,
            'phone_number': phone,
            'agent_email': email,
            'address': address,
            'city':city,
            'price': price
        }
            