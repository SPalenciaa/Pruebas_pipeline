@Test_Change_rates
Feature: Test_Change_rates

Background: 

    Given I am on the change rates page
    When I select "Chage-rates" of the company Identidad
@smoketest
@Test_Change_rates_1 
Scenario: Error when not sending empty rate changes (error)

    When I click the "save" button
    When I confirm the update of rates
    Then I see the error message "An error ocurred updating rates" in "//div[@class='ant-notification-notice-description']"

@Test_Change_rates_2
Scenario: Download csv of rates sms and voice
 
    When I click download csv of "SMS Rate Template"
    When I see a file downloaded "TemplateRates-SMS.csv"
    When I click download csv of "Voice Rate Template"
    When I see a file downloaded "TemplateRates-Voice"


@Test_Change_rates_3 
Scenario: View current rates Sms
 
    When I click the view current rates "sms" button
    Then I see a current rates "sms"

@Test_Change_rates_4 
Scenario: View current rates Voice
 
    When I click the view current rates "voice" button
    Then I see a current rates "voice"

@Test_Change_rates_5
Scenario: Chage_Rates Sms 
 
    When I upload the rate "draggerSms" archive "TemplateRates-SMS-pruebas.csv"
    When I click the "save" button
    When I confirm the update of rates
    When I am see the confirmation alert, "TRANSACTION SUCCESSFUL" in "//div[@class='ant-notification-notice-message']"

@Test_Change_rates_5_1 
Scenario: Chage_Rates Sms confirmation
    
    When I click the view current rates "sms" button
    When I see the efective rate now

Scenario: Chage_Rates (error)

@Test_Change_rates_6
Scenario: Chage_Rates Voice
 
    When I upload the rate "draggerVoice" archive "TemplateRates-Voice-pruebas.csv"
    When I click the "save" button
    When I confirm the update of rates
    When I am see the confirmation alert, "TRANSACTION SUCCESSFUL" in "//div[@class='ant-notification-notice-message']"

@Test_Change_rates_6_1 
Scenario: Chage_Rates Voice confirmation
    
    When I click the view current rates "voice" button
    When I see the efective rate now


@Test_Change_rates_7
Scenario: Chage_Rates Sms and Voice
 
    When I upload the voice_and__sms-rates archive "TemplateRates-SMS.csv", "TemplateRates-Voice.csv"
    When I click the "save" button
    When I confirm the update of rates
    When I am see the confirmation alert, "TRANSACTION SUCCESSFUL" in "//div[@class='ant-notification-notice-message']"

@Test_Change_rates_7_1
Scenario: Chage_Rates Sms and Voice (ERROR Update Rates)
 
    When I upload the voice_and__sms-rates archive "TEMPLATES RATES SMS.csv", "TEMPLATES RATES SMS.csv"
    When I click the "save" button
    When I confirm the update of rates
    When I am see the confirmation alert, "ERROR" in "//div[@class='ant-notification-notice-message']"