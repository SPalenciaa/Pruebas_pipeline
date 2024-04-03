@Test_Company_Users_Create_User
Feature: Test_Company_Users_Create_User

Background: 

    Given I am on the users company page

@Test_Company_Users_Create_User_1 @smoke_test
Scenario:create user formulary (error)

    When I click button for the create user
    When I see the create user screen
    When I click the create user button
    When I confirm the create user
    Then I see the error message "Please input the first name!" in "//div[contains(text(),'Please input the first name!')]"
    Then I see the error message "Please input the email!" in "//div[contains(text(),'Please input the email!')]"
    Then I see the error message "Please select the role!" in "//div[contains(text(),'Please select the role!')]"
    Then I see the error message "Please select the account!" in "//div[contains(text(),'Please select the account!')]"

@Test_Company_Users_Create_User_2
Scenario:create user formulary send name only (error)

    When I click button for the create user
    When I see the create user screen
    When I write the "Felipe" in "form_in_modal_firstname"
    When I click the create user button
    When I confirm the create user
    Then I see the error message "Please input the email!" in "//div[contains(text(),'Please input the email!')]"
    Then I see the error message "Please select the role!" in "//div[contains(text(),'Please select the role!')]"
    Then I see the error message "Please select the account!" in "//div[contains(text(),'Please select the account!')]"

@Test_Company_Users_Create_User_3
Scenario:create user formulary send email only (error)

    When I click button for the create user
    When I see the create user screen
    When I write the "Felipe@pruebasautmoidentidad.oli" in "form_in_modal_email"
    When I click the create user button
    When I confirm the create user
    Then I see the error message "Please input the first name!" in "//div[contains(text(),'Please input the first name!')]"
    Then I see the error message "Please select the role!" in "//div[contains(text(),'Please select the role!')]"
    Then I see the error message "Please select the account!" in "//div[contains(text(),'Please select the account!')]"

@Test_Company_Users_Create_User_4
Scenario:create user formulary select role only (error)

    When I click button for the create user
    When I see the create user screen
    When I select "Account" in "form_in_modal_role"
    When I click the create user button
    When I confirm the create user
    Then I see the error message "Please input the first name!" in "//div[contains(text(),'Please input the first name!')]"
    Then I see the error message "Please input the email!" in "//div[contains(text(),'Please input the email!')]"
    Then I see the error message "Please select the account!" in "//div[contains(text(),'Please select the account!')]"

@Test_Company_Users_Create_User_5 @smoke_test
Scenario:create user formulary select accounts only (error)

    When I click button for the create user
    When I see the create user screen
    When I select "QXTL" in "form_in_modal_accounts"
    When I click the create user button
    When I confirm the create user
    Then I see the error message "Please input the first name!" in "//div[contains(text(),'Please input the first name!')]"
    Then I see the error message "Please input the email!" in "//div[contains(text(),'Please input the email!')]"
    Then I see the error message "Please select the role!" in "//div[contains(text(),'Please select the role!')]"

@Test_Company_Users_Create_User_6 
Scenario:Create User Done (Error)

    When I click button for the create user
    When I see the create user screen
    When I write the "PRUEBAS" in "form_in_modal_firstname"
    When I write the "AUTOMATIZADAS" in "form_in_modal_lastname"
    When I write the "samaya@identidadtech.com" in "form_in_modal_email"
    When I write the "Pruebas Automatizadas" in "form_in_modal_description"
    When I write the "3167628372" in "form_in_modal_phone"
    When I select "Account" in "form_in_modal_role"
    When I select "Recursos Humans" in "form_in_modal_accounts"
    When I click the create user button
    When I confirm the create user
    Then I see the error message "ERROR" in "//div[@class='ant-notification-notice-message']"

@Test_Company_Users_Create_User_7
Scenario:Create User Done

    When I click button for the create user
    When I see the create user screen
    When I write the "PRUEBAS" in "form_in_modal_firstname"
    When I write the "AUTOMATIZADAS Eliminar" in "form_in_modal_lastname"
    When I write the "Eliziuyuiyxz@pruebasa.oiu" in "form_in_modal_email"
    When I write the "Pruebas Automatizadas" in "form_in_modal_description"
    When I write the "3167628372" in "form_in_modal_phone"
    When I select "Account" in "form_in_modal_role"
    When I select "Recursos Humans" in "form_in_modal_accounts"
    When I click the create user button
    When I confirm the create user
    When I am see the confirmation alert, "ERROR" in "//div[@class='ant-notification-notice-message']"