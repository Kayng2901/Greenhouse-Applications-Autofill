from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('Greenhouse url')

    page.fill('input[name="job_application[first_name]"]', 'Your First Name')
    page.fill('input[name="job_application[last_name]"]', 'Your Last Name')
    page.fill('input[name="job_application[email]"]', 'Your Email')
    page.fill('input[name="job_application[phone]"]', 'Your Phone')
    page.fill('input[name="job_application[answers_attributes][0][text_value]"]', 'Your Linked-In')

    input("Press Enter to close...")
    browser.close()
