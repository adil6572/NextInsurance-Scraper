import requests
import xmltodict
import json

def fetch_xml_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the URL: {e}")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def convert_xml_to_json(xml_content, json_file_name="sitemap.json"):
    try:
        xml_dict = xmltodict.parse(xml_content)
        json_content = json.dumps(xml_dict, indent=2)

        # Write JSON to a file
        with open(json_file_name, "w") as json_file:
            json_file.write(json_content)

        print(f"Sitemap successfully converted and saved as {json_file_name}")

    except Exception as e:
        print(f"An error occurred during XML to JSON conversion: {e}")

def extract_agent_urls(json_file_name="sitemap.json", txt_file_name="sitemap.txt"):
    AGENT_URLS = []

    with open(json_file_name, 'r') as fp:
        data = json.load(fp)

    urls = data.get("urlset", {}).get("url", [])

    with open(txt_file_name, 'w') as fp:
        for url in urls:
            components = url.get("loc", "").split("/agents/")[1].split("/")
            components.pop()

            if len(components) > 1:
                agent_url = url.get("loc", "")
                AGENT_URLS.append(agent_url)
                fp.write(f"{agent_url}\n")

    print(f"Total URLs: {len(AGENT_URLS)}")

def main():
    sitemap_url = "https://www.nextinsurance.com/agents/sitemap/"

    xml_data = fetch_xml_data(sitemap_url)

    if xml_data:
        convert_xml_to_json(xml_data)
        extract_agent_urls()

if __name__ == "__main__":
    main()
