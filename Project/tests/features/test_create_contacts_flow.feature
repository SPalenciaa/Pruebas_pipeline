@Test_Create_Contacts_Flow
Feature: Test_Create_Contacts_Flow

@Test_Create_Contacts_Flow_1 
Scenario: Verify creation campaing

    When I am on the confirmation contacts page 
    And I click the "done" button to finish the campaign creation process
    And I click the confirm campaign
    When I am see the confirmation alert, "TRANSACTION SUCCESSFUL" in "//div[@class='ant-notification-notice-message']"
    Then I am redirected to the list_gropus page
