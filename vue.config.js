// const IS_PRODUCTION = process.env.NODE_ENV === 'production'

module.exports = {
  outputDir: "dist",
  assetsDir: "static",

  devServer: {
    proxy: {
      "/api*": {
        // Forward frontend dev server request for /api to Django Rest Framework dev server
        target: "http://localhost:8000/"
      }
    }
  },

  configureWebpack: {
    devtool: "source-map"
  }
};
