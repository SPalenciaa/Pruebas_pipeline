@Test_Create_Campaign_Options_Send_Schedule_SMS_Bulk
Feature: Test_Create_Campaign_Options_Send_Schedule_SMS_Bulk

Background: 

    Given I am on the campaign settings page "Bulk SMS" in "SMS"

@Test_Create_Campaign_Options_Send_Schedule_SMS_Bulk_1 @smoke_test
Scenario: Create campaign with send now option (error)

    Given I select a company and a campaign name empty or invalid
    When I click on the "next" button to continue
    Then I see the error message "The account field is mandatory" in "//div[@class='ant-notification-notice-description']"

@Test_Create_Campaign_Options_Send_Schedule_SMS_Bulk_2 
Scenario: Create campaign with send now option

    Given I select a company, and a name for the test "PRUEBAS AUTOMATIZADAS"
    When I select Send now/schedule option "1"
    When I click on the "next" button to continue
    Then I am redirected to the destination creation page

@Test_Create_Campaign_Options_Send_Schedule_SMS_Bulk_3 
Scenario: Create campaign with schedule option (error)

    Given I select a company, and a name for the test "PRUEBAS AUTOMATIZADAS"
    When I select Send now/schedule option "2"
    When I click on the "next" button to continue
    Then I see the error message "You need to properly schedule the dates for the campaign" in "//div[@class='ant-notification-notice-description']"

@Test_Create_Campaign_Options_Send_Schedule_SMS_Bulk_4 
Scenario: Create campaign with schedule option (error whit percentage)

    Given I select a company, and a name for the test "PRUEBAS AUTOMATIZADAS"
    When I select Send now/schedule option "2"
    When I click the add phase
    Then I see the error message "The percentage can not be zero" in "(//div[@class='ant-notification-notice-description'])[1]"

@Test_Create_Campaign_Options_Send_Schedule_SMS_Bulk_5 
Scenario: Create campaign with schedule option (warning percentage 100%)

    Given I select a company, and a name for the test "PRUEBAS AUTOMATIZADAS"
    When I select Send now/schedule option "2"
    When I enter a percentage "100" in the phase
    When I click the add phase
    Then I see the error message "Please, check the percentages assigned to each phase; the total amount must be 100%" in "(//div[@class='ant-notification-notice-description'])[1]"

@Test_Create_Campaign_Options_Send_Schedule_SMS_Bulk_6 
Scenario: Create campaign with schedule option (error date )

    Given I select a company, and a name for the test "PRUEBAS AUTOMATIZADAS"
    When I select Send now/schedule option "2"
    When I enter a percentage "100" in the phase
    When I enter the today date in the phase
    When I click on the "next" button to continue
    Then I see the error message "All the phases should have a configured date" in "(//div[@class='ant-notification-notice-description'])[1]"

@Test_Create_Campaign_Options_Send_Schedule_SMS_Bulk_7
Scenario: Create campaign with schedule option

    Given I select a company, and a name for the test "PRUEBAS AUTOMATIZADAS"
    When I select Send now/schedule option "2"
    When I enter a percentage "50" in the phase
    When I enter the "today" date in the phase
    When I enter the "now" hour
    When I click the add phase
    When I enter a percentage "50" in the phase
    When I enter the "tomorrow" date in the phase
    When I enter the "tomorrow" hour
    When I click on the "next" button to continue
    Then I am redirected to the destination creation page

    