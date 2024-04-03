@smoketest
@Test_Select_Campaing_Menu_All
Feature: Test_Select_Campaing_Menu_All

Background:

    Given I am on the menu page

@Test_Select_Campaing_Menu_All_1
Scenario: Select Shortlinks from Campaings menu

    When I select "Shortlink" from the campaigns menu "SMS"
    Then I am redirected to the campaign settings page

@Test_Select_Campaing_Menu_All_2
Scenario: Select Build campaign from Campaings menu

    When I select "Bulk SMS" from the campaigns menu "SMS"
    Then I am redirected to the campaign settings page

@Test_Select_Campaing_Menu_All_3
Scenario: Select Build campaign from Campaings menu

    When I select "Bulk Voice" from the campaigns menu "Voice"
    Then I am redirected to the campaign settings page

@Test_Select_Campaing_Menu_All_4
Scenario: Select Build campaign from Campaings menu

    When I select "Shortlinks Metrics" from the campaigns menu "SMS"
    Then I am redirected to the Shortlinks page init