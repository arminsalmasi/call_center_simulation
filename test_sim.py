from playwright.sync_api import sync_playwright
import urllib.request
import json
import time

try:
    req = urllib.request.Request("http://localhost:8000/api/simulation/stop", method="POST")
    urllib.request.urlopen(req)
except Exception:
    pass

time.sleep(1)

def run_cuj(page):
    page.goto("http://localhost:8000")
    page.wait_for_timeout(500)

    # Start the simulation
    page.get_by_role("button", name="Start").click()
    page.wait_for_timeout(2000)

    # Take screenshot at the key moment while running
    page.screenshot(path="/home/jules/verification/screenshots/verification3.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
