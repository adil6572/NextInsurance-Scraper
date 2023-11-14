from playwright.sync_api import Playwright, sync_playwright
import csv
from bs4 import BeautifulSoup


with open('sitemap.txt', 'r') as fp:
    URLS = fp.read().split('\n')

# URLS=URLS[:100]
OUTPUT_CSV_FILENAME = 'agents_data.csv'

def extract_text(element, selector):
    try:
        return element.select_one(selector).text.strip()
    except AttributeError:
        return ''

def write_to_csv(csv_writer, url, item):
    csv_writer.writerow({ 'name': item['name'], 'address': item['address'], 'phone': item['phone'], 'email': item['email'],'url': url,})

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Open the CSV file only once for all iterations
    with open(OUTPUT_CSV_FILENAME, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=['name', 'address', 'phone', 'email','url'])
        csv_writer.writeheader()

        for url in URLS:
            try:
                page.goto(url)
                cards = page.locator(".e6vvd7u4 p").all()
                page.wait_for_load_state()

                for i in range(0, len(cards)):
                    cards[0].click()

                url = page.url
                content = page.content()
                soup = BeautifulSoup(content, 'html.parser')
                person_cards = soup.select('[role="person-card"]')

                for card in person_cards:
                    item = {'url': url.strip()}
                    item['name'] = extract_text(card, "h3.mb-4")
                    item['address'] = extract_text(card, "p.mb-4")
                    item['phone'] = extract_text(card, ".e6vvd7u0 p")
                    item['email'] = extract_text(card, ".ml-2").lower()

                    print(item)

                    # Write data to the CSV file using the function
                    write_to_csv(csv_writer, url, item)

            except Exception as e:
                print(f'Exception at agent pages {url}: {e}')

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
