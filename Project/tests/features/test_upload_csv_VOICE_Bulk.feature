@Test_Upload_Csv_Voice_Bulk
Feature: Test_Upload_Csv_Voice_Bulk

Background: 

    Given I am on the content creation page "Bulk Voice" in "Voice"

@Test_Upload_Csv_Voice_1
Scenario: Upload CSV file invalid (error)

    When I am not upload csv file
    When I click on the "next" button to continue
    Then I see the error message "You need to load a .CSV or Excel File" in "(//div[@class='ant-notification-notice-description'])[1]"

@Test_Upload_Csv_Voice_2 
Scenario: Unselect MobileNumber (error)

    When I upload a valid CSV file with phone numbers
    When I click on the "next" button to continue
    Then I see the error message "You need to select which column in the file contains the phone number" in "(//div[@class='ant-notification-notice-description'])[1]"
    And I click on the "remove file" button 

@Test_Upload_Csv_Voice_3 
Scenario: Upload CSV file

    When I upload a valid CSV file with phone numbers
    When I select the "MobileNumber" column from the CSV file
    When I select the wildcards to use
    When I click on the "next" button to continue
    Then I am redirected to the message content page

