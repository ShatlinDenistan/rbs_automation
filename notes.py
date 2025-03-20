from playwright.sync_api import expect, Page

# assert if an elements exists in a page
page = Page()
locator = page.locator("//button")
expect(locator).to_be_visible(timeout=5000)


# fill text
locator.fill("Hello world")

# type text
locator.type("Hello world")

# click
locator.click()
