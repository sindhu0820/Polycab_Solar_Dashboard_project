Feature:API

@api
   Scenario: Verify the Device Status Values
    Given I login to solar app
    And the API endpoint for device status is "http://solar.silvan.co.in:7880/solar/getInverterStatus?emailid=superadmin@gmail.com&secret=bed6c5f35535bb3e9eac5d754d6413a6"
    When I send a GET request to the endpoint
    Then the response status code should be 200
    And  the response should contain a "data"
    And the device status counts should match expected values "data"

@api
Scenario: Verifying Daily Production value
    Given I login to solar app
    And the API endpoint for Daily Production is "http://solar.silvan.co.in:7880/solarM/stats?emailid=superadmin@gmail.com&secret=1000a433b534721421b7ad3e9460b728"
    When I send a GET request to the endpoint
    Then the response status code should be 200
    And  the response should contain a "data"
    And the daily production value should match

@api
Scenario: Verifying the Peak Hour Rankings
    Given I login to solar app
    And the API endpoint for peak hour ranking is "http://solar.silvan.co.in:7880/solarM/peakHourRanking?emaiilid=superadmin@gmail.com&secret=1000a433b534721421b7ad3e9460b728&limit=10"
    When I send a GET request to the endpoint
    Then the response status code should be 200
    And  the response should contain a "data"
    And peak hour rankings should be displayed

@api
Scenario: Verifying the Power Normalization Rankings for top 10
  Given I login to solar app
    And the API endpoint for power normalization values is "http://solar.silvan.co.in:7880/solarM/powerNormalization?emailid=superadmin@gmail.com&secret=1000a433b534721421b7ad3e9460b728"
    When I send a GET request to the endpoint
    Then the response status code should be 200
    And  the response should contain a "data"
    And Top 10 power normalization values should be displayed
