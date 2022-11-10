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
  <form>
  <input v-model="zip" class="zip-searcher" />
  </form>
</template>

<style>
.zip-searcher {
  color: red;
  font-weight: bold;
}
</style>