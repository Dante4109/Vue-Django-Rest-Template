// Main Page - Cypress E2E Test
/// reference types="cypress" />

import { email } from "./setup.js";
import { password } from "./setup.js";

describe("Login", () => {
  beforeEach(() => {
    // Visit the main page before each test
    // This ensures that the login form is accessible
    cy.visit("/"); // Adjust the path to your main page if necessary
    cy.get('[data-cy="profile-btn-no-user"]').click(); // click to open login form
  });

  it("should log in with valid credentials", () => {
    // Fill in the login form
    cy.get('[data-cy="login-email-field"]').type(email);
    cy.get('[data-cy="login-password-field"]').type(password);
    cy.get('[data-cy="login-submit-btn"]').click();

    // Check if login was successful
    cy.get('[data-cy="profile-btn-user"]').should("be.visible");
  });
});
