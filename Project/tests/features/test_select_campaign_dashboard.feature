@test_campaign_dashboard
Feature: Test_select_create_campaign_dashboard_company_admin

Scenario Outline: Select create campaign

    Given I am in the dashboard page
    When I click <campaign_name> button in dashboard
    Then I am redirected to the firs step to create a SMS campaign

Examples:
| campaign_name |
| New SMS Campaign | 
| New VOICE Campaign | 

Scenario: Select Asign balance 
    Given I am in the dashboard page
    When I click "Assign Balance" button in dashboard
    Then I see the page of assign Balance

Scenario: Filter channel select dashboard

    Given I am in the dashboard page
    When I filter the channel for "All" in the dashboard
    Then I see the voice and SMS consumption at the same time

Scenario: Filter channel select dashboard

    Given I am in the dashboard page
    When I filter the channel for "Voice" in the dashboard
    Then I see only the voice consumption

Scenario: Filter channel select dashboard

    Given I am in the dashboard page
    When I filter the channel for "Sms" in the dashboard
    Then I filter only the consumption of sms

