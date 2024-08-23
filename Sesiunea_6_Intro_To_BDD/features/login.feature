Feature: Test the login page

  Background:
    Given I am on the login page
@login
  Scenario: Test valid login
    When I send a valid username and password
    And I press on the login button
    Then I am redirected to secure area page
    And I should see the banner: "You logged into a secure area!"
    And I should see the Logout button
@login
  Scenario: Test invalid login with correct username but wrong password
    When I send a correct username and wrong password
    And I press on the login button
    Then I should see the banner: "Your password is invalid!"
@login
  Scenario Outline: Test invalid login with wrong usernames and correct/wrong passwords
    When I send a wrong "<username>" and "<password>"
    And I press on the login button
    Then I should see the banner: "Your username is invalid!"
    Examples:
      | username | password |
      | tom321 | SuperSecretPassword!321 |
      | tom321 | SuperSecretPassword! |


