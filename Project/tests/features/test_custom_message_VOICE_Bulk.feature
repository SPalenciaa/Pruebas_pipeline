@Test_Custom_Message_VOICE_Bulk
Feature: Test_Custom_Message_VOICE_Bulk

Background:

    Given I am on the message creation page "Bulk Voice" in "Voice"

@Test_Custom_Message_VOICE_Bulk_1
Scenario: Create Custom Message empty (error)

    When I am not write nothing
    When I click on the "next" button to continue
    Then I see the error message "The sender ID is mandatory" in "//div[normalize-space()='The sender ID is mandatory']"

@Test_Custom_Message_VOICE_Bulk_2
Scenario: Create Custom Message only id (error)

    When I enter a valid campaign ID
    When I click on the "next" button to continue
    Then I see the error message "The message is mandatory" in "//div[normalize-space()='The message is mandatory']"

@Test_Custom_Message_VOICE_Bulk_3 
Scenario: Create Custom Message

    When I enter a valid campaign ID
    When I create a custom message with the wildcards and shortlink
    And I verify my message

@Test_Custom_Message_VOICE_Bulk_4
Scenario: Carrying out test campaign Message

    When I enter a valid campaign ID
    When I create a custom message with the wildcards
    When I select the "Female / English" voice for the campaign
    And I preview the message
    When I write the number for the test
    And I click on the "Verify Cost" button to continue
    When I see the cost of the message 
    And I click on the "send" button and confirm to continue
    When I am see the confirmation alert, "The message was successfully sent" in "(//div[@class='ant-notification-notice-description'])[1]"
    When I click on the "next" button to continue
    Then I am redirected to the summary page

@Test_Custom_Message_VOICE_Bulk_5
Scenario: BUG YP when we pass without selecting the voice of the call and we do a test test, the page stays loading https://identidadtech-team.monday.com/boards/5081280383/pulses/5385466403

    When I enter a valid campaign ID
    When I create a custom message with the wildcards
    When I click on the "next" button to continue
    Then I see the error message "The voice and gender are mandatory" in "(//div[@class='ant-notification-notice-description'])[1]"

    