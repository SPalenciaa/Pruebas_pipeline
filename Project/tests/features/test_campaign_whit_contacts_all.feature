@Test_Campaing_Whit_All_Contacts
Feature: Test_Campaing_Whit_All_Contacts

@Test_Campaing_Whit_All_Contacts_1
Scenario: Select contacts in the campaign Shortlinks

    Given I am on the content page "Shortlink" in "SMS"
    When I select the "PRUEBAS CONTACTOS" contacts file 
    When I click on the "next" button to continue
    When I enter a valid campaign ID and URL
    When I create a valid message
    When I click on the "next" button to continue
    And I click the "done" button to finish the campaign creation process
    And I click the confirm campaign
    When I am see the confirmation alert, "TRANSACTION SUCCESSFUL" in "//div[@class='ant-notification-notice-message']"
    Then I am redirected to the campaigns menu and see the confirmation alert



@Test_Campaing_Whit_All_Contacts_2
Scenario: Select contacts in the campaign Bulk

    Given I am on the content page "Bulk SMS" in "SMS"
    When I select the "PRUEBAS CONTACTOS" contacts file 
    When I click on the "next" button to continue
    When I enter a campaign ID 
    When I create a valid message
    When I click on the "next" button to continue
    And I click the "done" button to finish the campaign creation process
    And I click the confirm campaign
    When I am see the confirmation alert, "TRANSACTION SUCCESSFUL" in "//div[@class='ant-notification-notice-message']"
    Then I am redirected to the campaigns menu and see the confirmation alert

@Test_Campaing_Whit_All_Contacts_3
Scenario: Select contacts in the campaign Voice

    Given I am on the content page "Bulk Voice" in "Voice"
    When I select the "PRUEBAS CONTACTOS" contacts file 
    When I click on the "next" button to continue
    When I enter a campaign ID 
    When I create a valid message
    When I select the "Female / English" voice for the campaign
    When I click on the "next" button to continue
    And I click the "done" button to finish the campaign creation process
    And I click the confirm campaign
    When I am see the confirmation alert, "TRANSACTION SUCCESSFUL" in "//div[@class='ant-notification-notice-message']"
    Then I am redirected to the campaigns menu and see the confirmation alert