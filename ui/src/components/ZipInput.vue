<script>
import axios from 'axios'
</script>

<template>
  <h1>Zip Finder</h1><br/>
  <form action="http://127.0.0.1:8000/find-zip">
  <input v-model="zip" class="zip-searcher" />
  <button id="submit-button" type="submit">Search</button>
  </form>
</template>

<style>
.zip-searcher {
  width:80vw;
}
</style>