// Main Page - Cypress E2E Test
/// reference types="cypress" />

describe("Main Page", () => {
  beforeEach(() => {
    cy.visit("/"); // Adjust the path to your main page if necessary
  });

  it("should display the main page with a title", () => {
    cy.get("h1").should("contain.text", "Vuetify x Django");
  });

  it("see the login button in the top right", () => {
    cy.get("button").contains("class=mdi-login").should("exist");
  });
});
