import re
from playwright.sync_api import Page, expect


def test_saucedemo_loginlocked (page : Page) -> None:
    #Open Web Sauce Demo
    page.goto("https://www.saucedemo.com/")
    #username fill
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("locked_out_user")
    #password fill
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    #button login    
    page.locator("[data-test=\"login-button\"]").click()
    
    
    
    # --- VALIDASI AKHIR (Assertion) ---
    # Memastikan teks sukses muncul di layar sebagai tanda transaksi berhasil
    success_header = page.locator("[data-test=\"error\"]")
    expect(success_header).to_have_text("Epic sadface: Sorry, this user has been locked out.")
    print(">>> STATUS: Skenario Checkout Berhasil & Tervalidasi!")

 
