// Plugins
import AutoImport from "unplugin-auto-import/vite";
import Components from "unplugin-vue-components/vite";
import Fonts from "unplugin-fonts/vite";
import Layouts from "vite-plugin-vue-layouts";
import Vue from "@vitejs/plugin-vue";
import VueRouter from "unplugin-vue-router/vite";
import Vuetify, {transformAssetUrls} from "vite-plugin-vuetify";

// Utilities
import {defineConfig} from "vite";
import {fileURLToPath, URL} from "node:url";
import path from "path";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    VueRouter(),
    Layouts(),
    Vue({
      template: {transformAssetUrls},
    }),
    // https://github.com/vuetifyjs/vuetify-loader/tree/master/packages/vite-plugin#readme
    Vuetify({
      autoImport: true,
      styles: {
        configFile: "src/styles/settings.scss",
      },
    }),
    Components(),
    Fonts({
      google: {
        families: [
          {
            name: "Roboto",
            styles: "wght@100;300;400;500;700;900",
          },
        ],
      },
    }),
    AutoImport({
      imports: ["vue", "vue-router"],
      eslintrc: {
        enabled: true,
      },
      vueTemplate: true,
    }),
  ],
  define: {
    "process.env": {},
    __VUE_PROD_DEVTOOLS__: true,
  },
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
    extensions: [".js", ".json", ".jsx", ".mjs", ".ts", ".tsx", ".vue"],
  },
  server: {
    port: 3000,
  },
  root: path.resolve(__dirname),
  build: {
    outDir: "dist",
    emptyOutDir: true, // also necessary
    rollupOptions: {
      output: {
        chunkFileNames: "static/js/[name]-[hash].js",
        entryFileNames: "static/js/[name]-[hash].js",

        assetFileNames: ({name}) => {
          if (/\.(ico)$/.test(name ?? "")) {
            return "static/[name]-[hash][extname]";
          }

          if (/\.(gif|jpe?g|png|svg)$/.test(name ?? "")) {
            return "static/img/[name]-[hash][extname]";
          }

          if (/\.css$/.test(name ?? "")) {
            return "static/css/[name]-[hash][extname]";
          }

          if (/\.(ttf|eot|woff2|woff)$/.test(name ?? "")) {
            return "static/fonts/[name]-[hash][extname]";
          }

          // default value
          // ref: https://rollupjs.org/guide/en/#outputassetfilenames
          return "static/[name]-[hash][extname]";
        },
      },
    },
    terserOptions: {
      compress: {
        drop_console: false,
        drop_debugger: false,
      },
    },
  },
});
