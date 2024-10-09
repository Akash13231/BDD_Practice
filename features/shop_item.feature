Feature: Shopping item from protocommers site


  Scenario Outline: shop items
    Given page url is given "<url>"
    When Item want to purchase
    Then sucess message appears for second
    Examples: credentials
     |url|
     |https://rahulshettyacademy.com/angularpractice/|