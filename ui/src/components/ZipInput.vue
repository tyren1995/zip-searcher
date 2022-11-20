<script setup>
import axios from 'axios'
import { ref } from 'vue'

const zip = ref('');
const search = () => (
axios.post('http://127.0.0.1:8000/find-zip', {"zip" : zip.value})
);

</script>

<template>
  <h1>Zip Finder</h1><br/>
  <input v-model="zip" class="zip-searcher" />
  <button @click="search">Search</button>
</template>

<style>
.zip-searcher {
  width:80vw;
}
</style>