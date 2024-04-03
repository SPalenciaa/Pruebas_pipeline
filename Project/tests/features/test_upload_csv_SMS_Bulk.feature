@Test_Upload_Csv_SMS_Bulk
Feature: Test_Upload_Csv_SMS_Bulk

Background: 

    Given I am on the content creation page "Bulk SMS" in "SMS"

@Test_Upload_Csv_SMS_Bulk_1
Scenario: Upload CSV file invalid (error)

    When I am not upload csv file
    When I click on the "next" button to continue
    Then I see the error message "You need to load a .csv or Excel File" in "(//div[@class='ant-notification-notice-description'])[1]"

@Test_Upload_Csv_SMS_Bulk_2
Scenario: Unselect MobileNumber (error)

    When I upload a valid CSV file with phone numbers
    When I click on the "next" button to continue
    Then I see the error message "You need to select which column in the file contains the phone number" in "(//div[@class='ant-notification-notice-description'])[1]"
    And I click on the "remove file" button 

@Test_Upload_Csv_SMS_Bulk_3
Scenario: Upload CSV file

    When I upload a valid CSV file with phone numbers
    When I select the "MobileNumber" column from the CSV file
    When I select the wildcards to use
    When I click on the "next" button to continue
    Then I am redirected to the message content page

@Test_Upload_Csv_SMS_Bulk_4
Scenario: Dowload CSV

    When I click to download CSV template
    When I see an example of a file required for the platform has been downloaded
