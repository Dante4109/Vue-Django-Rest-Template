const { defineConfig } = require("cypress");

const envVars = require("dotenv").config({ path: "./.env" });
// Load environment variables from .env file

module.exports = defineConfig({
  component: {
    devServer: {
      framework: "vue",
      bundler: "vite",
    },
  },

  e2e: {
    baseUrl: "http://localhost:3000",
    setupNodeEvents(on, config) {
      config.env = {
        ...config.env,
        ...envVars.parsed, // Merge environment variables from .env file
      };
      return config;
      // implement node event listeners here
    },
  },
});
