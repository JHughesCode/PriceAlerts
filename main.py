from selenium import webdriver
import schedule
import time
import smtplib


def send_email():
    sender = "REDACTED"
    recipient = "REDACTED"
    password = "REDACTED"
    subject = "Macbook Price Alert"
    body = "The price of this Macbook has dipped below £2000! \nCheck it out at https://www.amazon.co.uk/Apple-MacBook-16-inch-10%E2%80%91core-16%E2%80%91core/dp/B09JQV24NM/ref=sr_1_3?crid=380AT6R12F3LC&keywords=macbook%2Bpro&qid=1653389595&sprefix=macbook%2Caps%2C130&sr=8-3&th=1"
"

    message = f"""From: Jade Hughes{sender}
    To: Jade Hughes{recipient}
    Subject: {subject}\n
    {body}
    """

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        print("Logged in...")
        server.sendmail(sender, recipient, message)
        print("Email has been sent!")

    except smtplib.SMTPAuthenticationError:
        print("unable to sign in")


def get_price():
    URL = "https://www.amazon.co.uk/Apple-MacBook-16-inch-10%E2%80%91core-16%E2%80%91core/dp/B09JQV24NM/ref=sr_1_3?crid=380AT6R12F3LC&keywords=macbook%2Bpro&qid=1653389595&sprefix=macbook%2Caps%2C130&sr=8-3&th=1"
    chromedriver = "/home/jade/Downloads/chromedriver"
    driver = webdriver.Chrome(chromedriver)
    driver.get(URL)
    price = driver.find_element_by_class_name("a-price-whole")
    #call sendemail
    print(f"The price of this Macbook is currently £{price.text}.")
    if price.text[0] == "1":
        print("The price is below £2000. An email alert will be sent.")
        send_email()

#run daily
### test ### schedule.every(30).seconds.do(get_price)
schedule.every().day.at("12:00").do(get_price)

while True:
    schedule.run_pending()
    time.sleep(1)

