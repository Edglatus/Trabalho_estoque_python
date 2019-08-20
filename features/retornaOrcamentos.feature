Feature: Budget Return
    In order to cash in a sales order
    As salesmen
    we'll get a registered budget

    Scenario Outline: Budget Return
        Given I have the budget id <id>
        And I have the new status <status>
        When I get the budget
        Then I see the text "success"
        And I see the new status <new_status>

    Examples:
        | id | status | new_status |
        | 1  | 1 | 1 |
        | 1  | 0 | 0 |
        | 2  | 1 | 1 |
        | 2  | 0 | 0 |

    Scenario Outline: Budget Return False ID
        Given I have the budget id <id>
        When I get the budget
        But I do not see the text "success"

    Examples:
        | id  |
        | 250 |
        | 480 |

    Scenario Outline: Budget Return False Status
        Given I have the budget id <id>
        And I have the new status <status>
        When I get the budget
        But I do not see the new status <new_status>

    Examples:
        | id | status | new_status |
        | 1  | 0 | 1 |
        | 2  | 1 | 0 |
