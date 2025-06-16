// Main Page - Cypress E2E Test
/// reference types="cypress" />

describe("Main Page", () => {
  beforeEach(() => {
    cy.visit("/"); // Adjust the path to your main page if necessary
  });

  it("should display the main page with a title", () => {
    cy.get("h1").should("contain.text", "Vuetify x Django");
  });

  it("should display the login button in the top right", () => {
    cy.get('[data-cy="profile-btn-no-user"]')
      .should("be.visible")
      .should("exist");
  });

  it("should open the login form when the profile icon is clicked", () => {
    cy.get('[data-cy="profile-btn-no-user"]').click();
    cy.get('[data-cy="login-form"]').should("exist");
  });
});
