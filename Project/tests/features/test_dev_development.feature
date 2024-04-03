@Smoke_Test
@Test_Dev_Development
Feature: Test_Dev_Api

Background:
    Given I am on the login page of the dev

@Test_Dev_Api_1 
Scenario Outline: Api test
    When I select <channel> from the Developers menu
    Then I am redirected to SMS API Key page 
    When I see the apis 
### 9- BUG YP Se pintan todas las opciones y no se actualizan entre cada una las api's keys en el usuario developer (copy) https://identidadtech-team.monday.com/boards/5081280383/pulses/5824710749
Examples:
| channel |
| SMS | 
| Voice | 

@Test_Dev_documentation_1 
Scenario: Api test 
    When I select "Documentation" from the Developers menu
    Then I am redirected to Documentation page 
    When I see the Documentation Api