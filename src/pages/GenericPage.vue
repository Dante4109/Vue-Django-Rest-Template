<template>
  <div style="padding:2em;">
      <v-layout column class="white--text">
        <v-row>
          <v-col cols="12">
            <h1>Product: {{ product[0].product.name }}</h1>
            <h1>Price: {{ product[0].product.price }}</h1>
          </v-col>
        </v-row>
      </v-layout>
  </div>
</template>


<script>
const products = [
  {
    path: "1",
    product: { name: "Product 1", price: "$500" }
  },
  {
    path: "2",
    product: { name: "Product 2", price: "$1000" }
  },
  {
    path: "3",
    product: { name: "Product 3", price: "$1500" }
  }
];
export default {
  name: "Product",
  props: ["productPath"],
  data() {
    return {
      product: {}
    };
  },
  created() {
    // look up the product
    const foundProduct = products.filter(product => {
      return product.path === this.productPath;
    });
    // if it exists, proceed
    if (foundProduct.length > 0) {
      this.product = foundProduct;
    } else {
      // otherwise, go to the 404 page
      this.$router.push("/404");
    }
  }   
};
</script>

<style lang="scss">
</style>