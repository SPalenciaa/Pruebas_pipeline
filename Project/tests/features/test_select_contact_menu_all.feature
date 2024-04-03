@Smoke_Test_1
@Test_Select_Contacts_Menu_All
Feature: Test_Select_Contacts_Menu_All

Background: 

    Given I am in the dashboard

@Smoke_Test_2
@Test_Select_Contacts_Menu_All
Scenario: Select Create from Contacts menu

    When I select "Create" from the contacts menu
    Then I am redirected to the contacts create page step

@Test_Select_Contacts_Menu_All_1
Scenario: Select List / Groups from Contacts menu

    When I select "Groups" from the contacts menu
    Then I am redirected to the contacts Groups/Lists page



