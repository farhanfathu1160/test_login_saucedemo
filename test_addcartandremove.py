import re
from playwright.sync_api import Page, expect

def test_add_and_remove_cart(page: Page) -> None:
    # 1. Buka website Saucedemo
    page.goto("https://www.saucedemo.com/")
    
    # 2. Proses Login
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    
    # Validasi login sukses
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # 3. Tambahkan semua item ke keranjang
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
    page.locator("[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()

    # --- VALIDASI 1: Cek apakah badge keranjang menunjukkan angka 6 ---
    cart_badge = page.locator("[data-test=\"shopping-cart-badge\"]")
    expect(cart_badge).to_have_text("6")
    print(">>> 6 Item Berhasil Masuk Keranjang!")

    # 4. Hapus kembali semua item dari keranjang
    page.locator("[data-test=\"remove-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"remove-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"remove-sauce-labs-bolt-t-shirt\"]").click()
    page.locator("[data-test=\"remove-sauce-labs-fleece-jacket\"]").click()
    page.locator("[data-test=\"remove-sauce-labs-onesie\"]").click()
    page.locator("[data-test=\"remove-test.allthethings()-t-shirt-(red)\"]").click()

    # --- VALIDASI 2: Cek apakah badge keranjang hilang (kosong) ---
    # Jika semua item dihapus, badge angka jumlah item di keranjang biasanya hilang dari DOM
    expect(page.locator("[data-test=\"shopping-cart-badge\"]")).not_to_be_visible()
    print(">>> Semua Item Berhasil Dihapus dari Keranjang!")