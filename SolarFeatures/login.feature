Feature: login functionality

  @login
  Scenario: Login with valid credentials
    Given I have navigted to login page
    When I entered valid email address and password into the valid fiels
    And I click on login button
    And I select the yes option
    Then I should be logged in


  @login
  Scenario: login with invalid email and valid password
    Given  I have navigted to login page
    When I have entered invalid email address and valid password into the fiels
    And I click on login button
    Then I should not be logged in and should get proper warning message

  @login
  Scenario: Login with valid email and invalid password
    Given I have navigted to login page
    When I have entered valid email address and invalid password into the fiels
    And I click on login button
    Then I should not be logged in and should get proper warning message

  @login
  Scenario: Login with invalid credentials
    Given I have navigted to login page
    When I have entered invalid email and password
    And I click on login button
    Then I should not be logged in and should get proper warning message

  @login_without
  Scenario: Login without entering any credentials
    Given I have navigted to login page
    When I have not entered email and password
    And I click on login button
    Then I should not be logged in and should get proper warning message that is Failed