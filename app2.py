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
    page.evaluate("""
        () => {
            let select = document.querySelector('select[name="job_application[answers_attributes][1][boolean_value]"]');
            select.value = '1'; // To say Yes, change it to '2' to say No
            select.dispatchEvent(new Event('change'));
        }
    """)
    page.evaluate("""
        () => {
            let select = document.querySelector('select[name="job_application[answers_attributes][2][boolean_value]"]');
            select.value = '1'; // To say Yes, change it to '2' to say No
            select.dispatchEvent(new Event('change'));
        }
    """)

    input("Press Enter to close...")
    browser.close()
