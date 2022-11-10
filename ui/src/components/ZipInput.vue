<script>
export default {
  data() {
    return {
      zip: null
    }
  }
}
</script>

<template>
  <h1>Zip Finder</h1><br/>
  <form>
  <input v-model="zip" class="zip-searcher" />
  </form>
</template>

<style>
.zip-searcher {
  width:80vw;
}
</style>