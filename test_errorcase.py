import re
from playwright.sync_api import Page, expect

def test_saucedemo_errorcase(page: Page) -> None:
    # 1. Buka Web Sauce Demo
    page.goto("https://www.saucedemo.com/")
    
    # 2. Proses Login
    page.locator('//*[@id="user-name"]').click()
    page.locator('//*[@id="user-name"]').fill("standard_user")
    page.locator('//*[@id="password"]').click()
    page.locator('//*[@id="password"]').fill("secret_sauce")
    page.locator('//*[@id="login-button"]').click()
    
    # Validasi Login Sukses
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # 3. Pilih produk & masuk keranjang
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    
    # 4. Input data diri
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("qwe")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("tyu")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill(112)
    page.locator("[data-test=\"continue\"]").click()
    
    # 5. Finish checkout
    page.locator("[data-test=\"finish\"]").click()

    # --- VALIDASI AKHIR (Assertion) ---
    # Memastikan teks sukses muncul di layar sebagai tanda transaksi berhasil
    success_header = page.locator("[data-test=\"complete-header\"]")
    expect(success_header).to_have_text("Thank you for your order!")
    print(">>> STATUS: Skenario Checkout Berhasil & Tervalidasi!")