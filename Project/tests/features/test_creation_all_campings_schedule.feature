@Smoke_Test
@Test_Creation_Campaing_Flows_schedule
Feature: Test_Creation_Campaing_flow

@Test_Creation_Campaing_1
Scenario Outline: Review Campaign Data


    Given I am on the "<campaigns>" campaign summary page test in "<channel>"
    When I review the "PRUEBAS AUTOMATIZADAS" and data
    And I click the "done" button to finish the campaign creation process
    And I click the confirm campaign
    When I am see the confirmation alert, "TRANSACTION SUCCESSFUL" in "//div[@class='ant-notification-notice-message']"
    Then I am redirected to the campaigns menu and see the confirmation alert

    Examples:
    | campaigns      || channel  |
    | Shortlink      || SMS      |
    | Bulk SMS       || SMS      |
    | Bulk Voice     || Voice    |