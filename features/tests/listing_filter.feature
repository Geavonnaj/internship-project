
Feature: Listing Filter

  Scenario: User can filter the Secondary deals by “want to sell” option
    Given Open signin page
    When Login to the page with (insert email) and (insert password)
    When Click on mobile testing secondary option
    When Click on secondary option at the left side menu
    When Verify soft.reelly.io is in search result url
    When Filter the products by "want to sell"
    Then Verify all cards have "for sale" tag







