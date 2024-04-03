@Test_List_Groups
Feature: Test_List_Groups

Background:

    Given I am on the "Groups" page

@Test_List_Groups_1
Scenario: Filter List/groups

    When I filter the contacts "Pruebas Demo"
    When I see the group of contacts with the name "Pruebas Demo" and their data


