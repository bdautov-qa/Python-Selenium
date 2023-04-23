"""
Smoke test
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.smoke
def test_smoke(browser):
    """
    Test case SMK-1
    """
    url = "https://testqastudio.me/"
    browser.get(url=url)
    