Feature: Validate square API using CSV data with Pandas

  @single_test
  Scenario: validate test squaring API with multiple inputs from CSV
    Given test data is loaded from "squares.csv"
    When API is called for each input
    Then Verify that the actual result should match the expected value for all rows
