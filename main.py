from playwright.sync_api import sync_playwright, Page
import json
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
from typing import List, Optional
from pydantic import BaseModel
import json
import platform
from finic import Finic
from typing import Dict, Any

API_KEY = os.getenv("API_KEY")
BROWSER_CDP_URL = f"wss://browser-521298051240.us-central1.run.app/ws?api_key={API_KEY}&browser_id=test_browser"

@Finic.entrypoint
def main(url: str):
    finic_client = Finic()
    
    context = finic_client.launch_browser_sync(headless=False, slow_mo=500)
        
    page = context.new_page()
    page.goto(url)

    context.close()