@Test_select_account
Feature: Test_select_account

Background: 

    Given I login in yp platform


@Test_select_account_1
Scenario: Bug YP, las cuentas no muestran ninguna información. (copy) https://identidadtech-team.monday.com/boards/5074630027/pulses/5523638202

    When I select "Accounts" of the menu lateral of the page
    Then I am view account page
    When I select a "4" Account
    Then I view Balance in "Recursos Humans" Account
    When I select a "5" Account
    Then I view Balance in "Angie Mendoza" Account
     #4 is QXTL account 
     #5 is IDENTIDAD account
