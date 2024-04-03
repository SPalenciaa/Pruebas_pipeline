@Test_Company_Balance_Filters
Feature: Test_Company_Balance_Filters

Background: 

    Given I am on the Balance company page

@Test_Company_Balance_Filters_1
Scenario: Filter campaign

    When Filter the "Angie Mendoza" account 
    Then I will see the card of the "Angie Mendoza" account

