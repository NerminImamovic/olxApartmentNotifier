# olxApartmentNotifier

Scraping tool to get newest apartment links with email notifications using GitHub Actions

Get links of latest apartments from the biggest ecommerce Bosnian site olx.ba

## Usage

In file `apartment_notify/scraper.py` replace value of the `url` with wanted. 

In repository settings `Action Settings` is needed to setup environment secrets: 

* `EMAIL_PASSWORD` - password related to eamil and username used to login on GitHub
* `SENDER_MAIL_USERNAME` - gmail from which email would be sent
* `SENDER_MAIL_PASSWORD` - password of sender gmail

Note:
It is needed to enable access for less secure apps on the gmail.

https://stackoverflow.com/questions/45886791/unable-to-login-to-gmail-imaplib-error-alert-please-log-in-via-your-web-brow/61021726#61021726

As machines where GitHub Actions are changing for every execution. We should enable access for les secure apps really often.
