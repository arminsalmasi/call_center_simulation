import os
import subprocess
import time
from playwright.sync_api import sync_playwright

def verify():
    # Start the server
    server_process = subprocess.Popen(
        ["python", "web/app.py"],
        env=dict(os.environ, PYTHONPATH=".")
    )
    time.sleep(2) # wait for server to start

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)

            # Start recording video
            context = browser.new_context(
                record_video_dir="/home/jules/verification/videos/",
                record_video_size={"width": 1280, "height": 720}
            )
            page = context.new_page()

            # Navigate to the app
            page.goto("http://localhost:8000")

            # Non-blocking strategy to capture loading state
            held_routes = []
            def handle_route(route):
                # hold the request open without blocking
                held_routes.append(route)

            # Intercept the API request
            page.route("**/api/simulation/start", handle_route)

            # Click the start button
            page.click("#start-btn")

            # Wait a moment for DOM to update and capture screenshot
            page.wait_for_timeout(500)

            # The button should now be in the loading state
            os.makedirs("/home/jules/verification/screenshots", exist_ok=True)
            screenshot_path = "/home/jules/verification/screenshots/verification.png"
            page.screenshot(path=screenshot_path)

            # Release the request so it can finish
            for route in held_routes:
                route.continue_()

            page.wait_for_timeout(500)

            # Close everything
            page.close()
            context.close()
            browser.close()

            print(f"Screenshot saved to {screenshot_path}")
    finally:
        server_process.terminate()
        server_process.wait()

if __name__ == "__main__":
    verify()
