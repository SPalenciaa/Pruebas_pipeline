@Test_Add_Balance
Feature: Test_Add_Balance

Background: 

    Given I go to the exchange rate to add balance to the company Identity
    When I click the add balance button

@Test_Add_Balance_1
Scenario: Add 100 balance

    When I write "1" usd add balance
    When I confirm the add balance 
    When I am see the confirmation alert, "TRANSACTION SUCCESSFUL" in "//div[@class='ant-notification-notice-message']"
@smoketest
@Test_Add_Balance_2 
Scenario: Add 0 balance (error)
 

    When I confirm the add balance 
    When I see the alert error "Please input the balance!"


@Test_Add_Balance_3
Scenario: Add 1000000000000000 balance (error)
 
    When I write "100000000000000000000000000000" usd add balance
    When I confirm the add balance 
    Then I see the error message "An error ocurred adding balance" in "//div[@class='ant-notification-notice-description']"
