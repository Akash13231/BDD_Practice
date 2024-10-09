Feature: form fill


  Scenario Outline: fill the form
    Given url is given "<url>"
    When all date for form fill entered "<firstname>", "<email>", "<gender>", "<dob>", "<passw>"
    Then sucess message appears
    Examples: credentials
      |firstname | email | gender | dob | passw|url|
      |ABCDEF     | abc@.com|Male  |01/01/2001|abc@123|https://rahulshettyacademy.com/angularpractice/|
      |GHIJKL    |abc@.com |Female|01/01/2001|abc@123|https://rahulshettyacademy.com/angularpractice/|







