Feature: Emag cart feature

    Background:
      Given home: I am a user on emag.ro Home page
      When home: I search after "Pampers Premium Care nr 5"
      When products: I add product to basket "Scutece-chilotel Pampers Premium Care Pants XXL Box Marimea 5, 12-17 kg, 80 buc"
      When products: I click Vezi detalii cos

    @cart1
    Scenario: Test cart total sum functionality
      Then cart: I verify that total price is correct "129.64"


    @cart2
    Scenario: Test cart remove product functionality
      When cart: I click sterge link
      Then cart: I verify empty cart message is displayed




