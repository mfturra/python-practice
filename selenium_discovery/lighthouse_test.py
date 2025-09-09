import csv
import json
import os
import subprocess
import time
from urllib.parse import parse_qs, urlparse

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# -----Lighthouse helper----- #
def run_lighthouse(url: str, port: int = 9222) -> dict:
    """
    Launch Lighthouse against open Chrome tab
    Output: Dict with key metrics
    """
    lighthouse_cmd = [
        "lighthouse",
        url,
        "--output=json",
        "--output-path=stdout",
        f"--port={port}",
        "--quiet",
        "--disable-storage-reset",
        "--throttling-method=provided",
    ]

    proc = subprocess.run(
        lighthouse_cmd,
        capture_output=True,
        text=True,
        check=True
    )

    lh_json = json.loads(proc.stdout)
    audits = lh_json["audits"]

    # Lighthouse map audit keys
    return {
        "fcp": audits["first-contentful-paint"]["numericValue"],
        "tti": audits["interactive"]["numericValue"],
        "ttfb": audits["time-to-first-byte"]["numericValue"],
        "loadEventTime": audits["speed-index"]["numericValue"],
        "dcl": audits["dom-content-loaded"]["numericValue"],
    }

# ----- CSV / logging helpers ----- #
def save_metrics_to_csv(writer, stage_title, metrics):
    writer.writerow([stage_title])
    writer.writerow(["FCP (ms)", "TTI (ms)", "TTFB (ms)", "LET (ms)", "DCL (ms)"])
    writer.writerow(
        [
            metrics["fcp"],
            metrics["tti"],
            metrics["ttfb"],
            metrics["loadEventTime"],
            metrics["dcl"],
        ]
    )
    writer.writerow([])

def log_metrics(driver, stage_title, csv_writer=None, port=9222):
    metrics = run_lighthouse(driver.current_url, port)
    print(f"\nMetrics after {stage_title}:")
    print(f"First Contentful Paint: {metrics['fcp']:.2f} ms")
    print(f"Time to Interactive:   {metrics['tti']:.2f} ms")
    print(f"Time to First Byte:    {metrics['ttfb']:.2f} ms")
    print(f"Load Event Time:       {metrics['loadEventTime']:.2f} ms")
    print(f"DOMContentLoaded:      {metrics['dcl']:.2f} ms")

    if csv_writer:
        save_metrics_to_csv(csv_writer, stage_title, metrics)


# ----- Pytest fixture for Selenium ----- #
@pytest.fixture(scope="session")
def driver():
    debug_port = 9222
    opts = webdriver.ChromeOptions()
    opts.add_argument(f"--remote-debugging-port={debug_port}")
    opts.add_argument("--headless=new")  # new mode removes GPU dep
    opts.add_argument("--window-size=1920,1080")

    drv = webdriver.Chrome(options=opts)
    drv.set_page_load_timeout(60)
    yield drv
    drv.quit()


# ----- Automation Test ----- #
def test_account_login(driver):
    debug_port = 9222
    domain = os.getenv("DOMAIN")
    test_user = os.getenv("TESTUSER")
    password = os.getenv("PASSWORD")

    driver.get(domain)
    time.sleep(2)

    with open("performance_metrics.csv", mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        # ---- Stage 1: public login page ----
        log_metrics(driver, "Okta OAuth Page", csv_writer, port=debug_port)

        # ---- Stage 2: username entry ----
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "input28"))
        )
        driver.find_element(By.ID, "input28").send_keys(test_user)
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        log_metrics(
            driver,
            "User Credentials OAuth Page",
            csv_writer,
            port=debug_port,
        )

        # ---- Stage 3: password entry ----
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "input53"))
        )
        driver.find_element(By.ID, "input53").send_keys(password)
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        log_metrics(driver, "Password OAuth Page", csv_writer, port=debug_port)

        print("\nLogin complete.")

        # ---- Stage 4: post-login landing page ----
        log_metrics(driver, "Post-Login Page", csv_writer, port=debug_port)