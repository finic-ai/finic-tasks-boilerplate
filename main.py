from playwright.sync_api import sync_playwright, Page
from finic_py import Finic

finic = Finic()

@finic.entrypoint
def main(input_data: dict):
    """Main function to run the automation"""
    page, context = finic.launch_browser_sync(headless=False, slow_mo=500)
if __name__ == "__main__":
    main()