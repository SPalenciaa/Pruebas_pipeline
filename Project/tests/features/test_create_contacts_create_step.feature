@Test_Create_Contacts_Create_Step
Feature: Test_Create_Contacts_Create_Step

Background: 

    Given I am on the contacts "Create" page

@Test_Create_Contacts_Create_Step_1 @smoke_test
Scenario: Create contacts data empty (error)

    When I am not write the list name
    When I click on the "next" button to continue
    Then I see the error message "This field is mandatory" in "//div[contains(text(),'This field is mandatory')]"

@Test_Create_Contacts_Create_Step_2 @smoke_test
Scenario: Create contacts whit list name (error)

    When I write the name for the list name "PRUEBAS CONTACTOS"
    When I click on the "next" button to continue
    Then I see the error message "You need to select an account" in "//div[@class='ant-notification-notice-description']"

@Test_Create_Contacts_Create_Step_3 
Scenario: Upload CSV file invalid (error)

    When I write the name for the list name "PRUEBAS CONTACTOS"
    When I select the account "Identidad"
    When I click on the "next" button to continue
    Then I see the error message "You need to upload a file" in "//div[@class='ant-notification-notice-description']"

@Test_Create_Contacts_Create_Step_4 
Scenario: Create contacts create step

    When I write the name for the list name "PRUEBAS CONTACTOS"
    When I select the account "Identidad"
    When I upload a valid CSV file with phone numbers
    When I click on the "next" button to continue
    When I redirect at the map page

   