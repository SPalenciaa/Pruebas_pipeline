@Test_Custom_Message_SMS_Bulk
Feature: Test_Custom_Message_SMS_Bulk

Background: 

    Given I am on the message creation page "Bulk SMS" in "SMS"

@Test_Custom_Message_SMS_Bulk_1 
Scenario: Create Custom Message empty (error)

    When I am not write nothing
    When I click on the "next" button to continue
    Then I see the error message "The sender ID is mandatory" in "//div[normalize-space()='The sender ID is mandatory']"

@Test_Custom_Message_SMS_Bulk_2 
Scenario: Create Custom Message only id (error)

    When I enter a valid campaign ID
    When I click on the "next" button to continue
    Then I see the error message "The message is mandatory" in "//div[normalize-space()='The message is mandatory']"

@Test_Custom_Message_SMS_Bulk_3 
Scenario: Create Custom Message

    When I enter a valid campaign ID
    When I create a custom message with the wildcards and shortlink
    And I verify my message

@Test_Custom_Message_SMS_Bulk_4
Scenario: Carrying out test campaign Message    
    When I enter a valid campaign ID
    When I create a custom message with the wildcards
    And I verify my message
    When I write the number for the test
    And I click on the "Verify Cost" button to continue
    When I see the cost of the message
    And I click on the "send" button and confirm to continue 
    When I am see the confirmation alert, "The message was successfully sent" in "(//div[@class='ant-notification-notice-description'])[1]"
    When I click on the "next" button to continue
    Then I am redirected to the summary page