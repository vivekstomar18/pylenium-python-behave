Feature: Create product, get product, and add to cart using data from CSV

  Scenario: Validate product creation and add to cart for all rows in CSV
    Given test data is loaded from "products.csv"
    When each product is created, retrieved, validated, and added to cart
    Then all products should appear in their respective cart responses
