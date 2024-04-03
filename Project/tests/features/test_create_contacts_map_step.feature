@Test_Create_Contacts_Map_Step
Feature: Test_Create_Contacts_Map_Step

Background:

Given I am on the create contacts map page

@Test_Create_Contacts_Map_Step_1
Scenario: Unselect MobileNumber (error)
    When I click on the "next" button to continue
    Then I see the error message "You need to select the column that contains the phone number" in "(//div[@class='ant-notification-notice-description'])[1]"

@Test_Create_Contacts_Map_Step_2 
Scenario: Select mobile number and the wildcards
    When I select "MobileNumber" of the csv
    When I select the wildcards to use
    When I click on the "next" button to continue
    When I redirect at the confirmation page