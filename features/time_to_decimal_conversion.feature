Feature: Decimal time to Timestamp conversions

    Scenario Outline: decimal time to timestamp
        Given the timestamp <timestamp>
        When the input is valid
        Then it is converted to a decimal representation of the time <decimal>

        Examples:
        |timestamp | decimal |
        |"08:30:00"| 8.5     |
        |"17:00:00"| 17      |
        |"21:45:00"| 21.74   |

    Scenario Outline: timestamp to decimal time
        Given the decimal representation of the time <decimal>
        When the input is valid
        Then it is converted to a timestamp <timestamp>

        Examples:
        |timestamp | decimal |
        |"08:30:00"| 8.5     |
        |"17:00:00"| 17      |
        |"21:45:00"| 21.74   |

    Scenario Outline: invalid timestamp
      Given the timestamp <timestamp>
      When the input is not valid
      Then the error message '<error>' is shown

      Examples:
      |timestamp | error                      |
      |"28:30:00"| 'This is not a valid time' |
      |"17:00:00"| 'This is not a valid time' |
      |"21:45:00"| 'This is not a valid time' |

    Scenario Outline: invalid decimal time
      Given the decimal representation of the time <decimal>
      When the input is not valid
      Then the error message '<error>' is shown

      Examples:
      |decimal | error                      |
      |28      | 'This is not a valid time' |
      |-1      | 'This is not a valid time' |
      |200000  | 'This is not a valid time' |
