Feature: form fill


  Scenario Outline: fill the form
    When all date for form fill given "<firstname>", "<email>", "<gender>", "<dob>", "<passw>"
    Then sucess message appears
    Examples: credentials
      |firstname | email | gender | dob|passw|
      |akash     | abc@.com|Male  |01/01/2001|abc@123|
      |Tejashvini|abc@.com |Female|01/01/2001|abc@123|
      |prasad    |abc@.com |Male  |01/01/2001|abc@123|