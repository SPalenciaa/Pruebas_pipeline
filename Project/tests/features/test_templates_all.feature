@Test_Templates_Menu_All
Feature: Test_Select_Contacts_Menu_All

Background: 

    Given I am on the yp dashboard

@Test_Select_Templates_1
Scenario: Select History from Templates menu

    When I select "History" from the Templates menu
    Then I am redirected to the History Templates page step
    When I see the templates "Prueba Test"

@Test_Select_Templates_2
Scenario: Filter templates
    When I select "History" from the Templates menu
    Then I am redirected to the History Templates page step
    When I filter "Angie pruebas"
    When I see the template "Angie pruebas"





