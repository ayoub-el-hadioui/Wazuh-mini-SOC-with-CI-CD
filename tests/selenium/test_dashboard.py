from selenium import webdriver

def test_dashboard_login_page():
    driver = webdriver.Chrome()
    driver.get("https://your-domain/")
    assert "Wazuh" in driver.title
    assert driver.find_element("id", "username")
    driver.quit()
