# NextInsurance Agent Scraper

## Table of Contents

- [Description](#description)
- [Task](#task)
- [Objective](#objective)
- [Methodology](#methodology)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Description

This repository includes a scraper designed to extract contact information for agents from NextInsurance.com, an innovative online platform revolutionizing insurance for businesses of all sizes. The platform provides a user-friendly interface and a range of customized insurance solutions, streamlining the coverage process, from liability to workers' compensation.

## Task

The primary task of this scraper is to efficiently collect contact details of agents listed on the NextInsurance website.

## Objective

The overarching goal of this project is to create a robust scraper capable of navigating the dynamic content on the NextInsurance website and extracting relevant contact information for agents.

## Methodology

To tackle the dynamic nature of the website, the following methodology is employed:

1. **Browsing**: Utilizing Playwright in Python to simulate browser actions and navigate through dynamically loaded content.
2. **Sitemap.xml**: Utilizing the sitemap.xml file to locate all the agents link on site
3. **Data Extraction**: Employing Beautiful Soup to parse and extract the requisite contact information after page loading.
4. **Output**: Saving the scraped data as a CSV file for subsequent analysis.

## Dependencies

Ensure the following dependencies are installed before running the scraper:

- Python (version >= 3.6)
- Playwright (`pip install playwright`)
- BeautifulSoup (`pip install beautifulsoup4`)

## Usage

**Clone this repository:**

```bash
git clone https://github.com/adil6572/NextInsurance-Scraper.git
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Execute the scraper:**

Before running the main scraper, execute the `sitemap.py` file first. This script extracts all agent URLs from the sitemap and performs necessary cleaning. It generates the `sitemap.txt` file containing URLs of all agents on the site.

```bash
python sitemap.py
```

Once the sitemap is generated, proceed to run the main scraper:

```bash
python main.py
```

Ensure that the sitemap file (`sitemap.txt`) is present in the project directory before executing the main scraper. This sequence ensures the necessary data is prepared for the main scraper to efficiently collect contact details of agents from the [NextInsurance](https://www.nextinsurance.com/agents) website.

## Output

The output CSV file, named `agent_data.csv`, follows the format below:

Each row in the CSV file represents an item with the following fields:

- **Name**: The name associated with the agent.
- **Address**: The agent's address.
- **Phone**: The agent's phone number.
- **Email**: The agent's email address.
- **URL**: The URL associated with the agent.

This format is maintained consistently throughout the CSV file. If you want to change the output filename in `main.py`, you can do so by modifying the variable where the filename is specified, for example:

```python
OUTPUT_CSV_FILENAME  =  'agents_data.csv'
```

## Contributing

Contributions are welcomed! Please feel free to open issues or pull requests to enhance the functionality of the scraper.

## License

This project is licensed under the [MIT License](LICENSE).
