from Sesiunea_6_Intro_To_BDD.browser import Browser


class BasePage(Browser):
    def navigate_to_main_page(self):
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")
