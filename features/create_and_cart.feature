
Feature: Create product, get product, and add to cart

  Scenario Outline: Validate that new item is created and added to the cart.
    Given New product is created with "<title>", price "<price>", description "<description>", and category "<category>"
    When the created product is retrieved
    And Correct product details are displayed containing title "<title>" and price "<price>"
    And the product is added to the cart
    Then Verify that the product is added and displayed in the cart details page

    Examples:
      | title     | price | description | category    |
      | product A | 99.99 | Desc A      | electronics |
      | product B | 49.50 | Desc B      | clothing    |
      | product C | 10.00 | Desc C      | toys        |

