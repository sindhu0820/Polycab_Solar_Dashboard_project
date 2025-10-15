Feature:HomePage

  @home
  Scenario: Verifiying the heading on homePage
     Given Navigate to login page
     When  I login to solar app
     Then Solar Monitoring Dashboard should be visible

  @home
  Scenario: Verifying the background color
    Given Navigate to login page
    When  I login to solar app
    And If i select light
    Then the light mode should be visible

  @home
  Scenario: Verifying the background color
    Given Navigate to login page
    When  I login to solar app
    And If i select dark
    Then the dark mode should be visible

  @home
   Scenario: Verifying the settings icon
    Given Navigate to login page
    When  I login to solar app
    And If i click on setting icon
    Then profile and logout option should be visible

   @home
   Scenario: Verifying the existance of the features
     Given Navigate to login page
     When  I login to solar app
     Then Production Overview, Device Status, Historical Production, Peak Hour Rankings, Overall Planned Production and Power Normalization Rankings should exist.

   @home
   Scenario: Verifying the existence of the features under Production Overview
     Given Navigate to login page
     When  I login to solar app
     Then Daily, Monthly, Yearly and total production and Total Plants Capacity should be visible

   @home
   Scenario: Verifying the existence of the features under Device Status
     Given Navigate to login page
     When  I login to solar app
     Then Total, Online, Offline and Incomplete Inverters should be visible

   @home-Total
   Scenario: Verifying the Total Inverters
     Given Navigate to login page
     When  I login to solar app
     Then By adding the Online, Offline and Incomplete Inverters should be equal to Total Inverters

