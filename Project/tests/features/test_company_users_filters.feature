@Test_Company_Users_Filters
Feature: Test_Company_Users_Filters

Background: 

    Given I am on the users company page

@Test_Company_Users_Filters_1
Scenario: Filter users

    When Filter the "developer 2 felipe" usersname
    Then I will see the card of the "vahani4883@fkcod.com" user email