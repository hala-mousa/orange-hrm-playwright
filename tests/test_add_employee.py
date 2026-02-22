from playwright.sync_api import Page, expect

def test_add_employee(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("link", name="PIM").click()
    page.get_by_role("button", name="Add").click()

    page.get_by_placeholder("First Name").fill("Halaa")
    page.get_by_placeholder("Last Name").fill("Mousa")

    page.get_by_role("button", name="Save").click()

    expect(page.get_by_role("heading", name="Personal Details")).to_be_visible(timeout=15000)