# Webscraping Homes.com for Agent Details

This project aims to scrape agent details from the Homes.com website using Scrapy and Selenium. The website renders its content with JavaScript, making it necessary to use both Scrapy and Selenium to ensure accurate data extraction.

## Objective
The objective of this project is to collect information about real estate agents, including the name of the agency, the first and last name of the agent, agent phone number and email, address, city, and price of listings.

## Tools Used
- **Scrapy**: A Python framework for web scraping. It provides powerful features for extracting data from websites.
- **Selenium**: Used in conjunction with Scrapy to scrape websites that render content using JavaScript.
- **CSV**: The scraped data is saved to a CSV file for further analysis and processing.

## Process
1. **Setup Environment**: Install Scrapy and Selenium in your Python environment.
2. **Create Scrapy Project**: Initialize a new Scrapy project using the `scrapy startproject` command.
3. **Define Spider**: Write a spider to navigate the Homes.com website, extract agent details, and follow pagination to scrape multiple pages.
4. **Handle JavaScript Rendering**: Use Selenium to handle pages where content is rendered using JavaScript. This ensures that all data is properly loaded and accessible.
5. **Extract Data**: Use XPath or CSS selectors to locate and extract relevant information from the webpage.
6. **Save Data**: Save the extracted data to a CSV file for further analysis and processing.
7. **Testing and Debugging**: Test the spider on sample pages, debug any issues, and refine the scraping process as needed.
8. **Scalability**: Optimize the spider for performance and scalability, considering factors such as handling rate limiting and avoiding IP bans.

## Usage
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Scrapy spider using the command `scrapy crawl <spider_name>`.
4. The scraped data will be saved to a CSV file in the output directory.

## Disclaimer
Please note that web scraping may be subject to legal restrictions and the terms of service of the website being scraped. Ensure compliance with all applicable laws and regulations before scraping any website.

## Contributing
Contributions and feedback are welcome! Feel free to submit issues or pull requests to improve this project.

---

By following the steps outlined above, you can effectively scrape agent details from the Homes.com website using Scrapy and Selenium. This README provides a comprehensive overview of the project, including the tools used, the scraping process, and instructions for usage and contribution.

### website view

![image](https://github.com/FaeyO/webscrapping-agent-details-from-homes.com-website/assets/118575325/36ac2df2-a6ac-40b4-bd5d-6bfb0f8e0b57)
