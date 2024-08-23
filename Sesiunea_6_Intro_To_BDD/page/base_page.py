from browser import Browser


class BasePage(Browser):
    def navigate_to_main_page(self):
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")

    def navigate_to_login_page(self):
        self.chrome.get("https://the-internet.herokuapp.com/login")