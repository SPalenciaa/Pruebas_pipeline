@smoke_Test
@Test_Rol_All
Feature: Test_Rol_All

@Test_Rol_All_1
Scenario Outline: Login with different roles
    Given I am on the login page
    When I enter <username> and <password>
    And I click the "Next" button
    When I should be logged in successfully
    And I should see my <username> and <role> displayed on the screen

Examples:
| username | password | role |
| development@identidadtech.com | Identidad123* | Admin |
| cbarbosa@identidadtech.com | Pruebas123* | CompanyAdmin |
| dmendez@identidadtech.com | Pruebas123* | user |
    

