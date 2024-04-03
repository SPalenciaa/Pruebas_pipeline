@Smoke_Test
@Test_Select_Company_All
Feature: Test_Select_Company_All

Background: 

    Given I am on the initial menu and click in "Company Home"

@Test_Select_Company_All_1 @smoke_test
Scenario: Select Company-Account from Company menu

    When I select "Accounts" from the company-Home menu
    Then I am redirected to the campaign Account page

@Test_Select_Company_All_2 @smoke_test
Scenario: Select Company-Users from Company menu

    When I select "Users" from the company-Home menu
    Then I am redirected to the campaign Users page

@Test_Select_Company_All_3 @smoke_test
Scenario: Select Company-Rates from Company menu

    When I select "Rates" from the company-Home menu
    Then I am redirected to the campaign Rates page

@Test_Select_Company_All_4 @smoke_test
Scenario: Select Company-History_Balance from Company menu

    When I select "Balance History" from the company-Home menu
    Then I am redirected to the campaign History Balance page