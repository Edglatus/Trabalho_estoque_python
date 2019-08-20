Feature: Cash Budget
    In order to cash in a sales order
    As salesmen
    we'll destock an order

    Scenario Outline: cash budget
        Given I have the budget id <id>
        When I cash the budget
        Then I see the text "success"

    Examples:
        | id |
        | 1  |
        | 2  |

    Scenario Outline: Cash Budget Fail
        Given I have the budget id <id>
        When I cash the budget
        Then I do not see the text "success"

    Examples:
        | id  |
        | 3   |
        | 420 |
