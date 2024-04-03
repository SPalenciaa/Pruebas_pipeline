@Test_Company_Balance_Assign_Credits
Feature: Test_Company_Balance_Assign_Credits

Background: 

    Given I am on the Balance company page
@smoketest
@Test_Company_Balance_Assign_Credits_1
Scenario: Asign credit accounts (error)

    When I select "Assign Credit" button 
    Then I see the assign credits screen
    When I click the "Allocate founds" button
    Then I see the error message "You need to select an account" in "//div[@class='ant-notification-notice-description']"

@Test_Company_Balance_Assign_Credits_2
Scenario: Asign credit accounts (error)

    When I select "Assign Credit" button 
    Then I see the assign credits screen
    When I select the "Identidad" account
    When I click the "Allocate founds" button
    Then I see the error message "The value must be greater than zero" in "//div[@class='ant-notification-notice-description']"

@Test_Company_Balance_Assign_Credits_3
Scenario: Asign credit accounts (error)

    When I select "Assign Credit" button 
    Then I see the assign credits screen
    When I select the "Identidad" account
    When I enter a valor "-10" in the avaliable balanace
    When I click the "Allocate founds" button
    Then I see the error message "An error occurred while transferring balance among accounts" in "//div[@class='ant-notification-notice-description']"

@Test_Company_Balance_Assign_Credits_4
Scenario: Asign credit accounts tecnologia->Identidad

    When I select "Assign Credit" button 
    Then I see the assign credits screen
    When I select the "Identidad" account
    When I enter a valor "10" in the avaliable balanace
    When I click the "Allocate founds" button
    When I am see the confirmation alert, "The balance transfer among accounts was successful" in "(//div[@class='ant-notification-notice-description'])[1]"