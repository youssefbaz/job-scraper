# Job Scraper using Selenium

This repository contains a Python script that uses Selenium to scrape job listings from the Apec website. The script collects various details about job offers, including the title, company, description, salary, contract type, location, and publication date, and then saves this information into a CSV file.

## Features

- Scrapes job listings from Apec.
- Extracts job details like title, company, description, salary, contract type, location, and publication date.
- Saves the scraped data into a CSV file.

## Prerequisites

- Python 3.x
- Chrome WebDriver (Make sure the version matches your Chrome browser version)
- Required Python packages: `selenium`, `pandas`

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/job-scraper.git
    cd job-scraper
    ```

2. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download ChromeDriver**:
   - Ensure that the ChromeDriver version matches your installed Chrome browser version.
   - Place the `chromedriver.exe` file in the same directory as the script or specify the path in the script.

## Usage

1. **Run the script**:
    ```bash
    python job_scraper.py
    ```

2. The script will automatically navigate through the Apec job search pages and scrape the required information.

3. **Output**:
   - The scraped data will be saved into a CSV file named `Jobs_Apex.csv`.

## Notes

- The script currently scrapes the first 10 pages of the job search results.
- You can modify the `page range` in the script to scrape more or fewer pages.
- Ensure your internet connection is stable, as the script relies on live web scraping.

## Troubleshooting

- If you encounter issues with ChromeDriver, ensure that the version of ChromeDriver matches the version of the Chrome browser installed on your machine.
- If elements are not found, it might be due to changes in the website structure. Update the `By` selectors as necessary.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Contact

If you have any questions or issues, please create an issue in this repository.

