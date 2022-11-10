<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
<div id="wrapper">
  <RouterView />
</div>
</template>

<style >
#wrapper{
  display: flex;
  height: 100vh;
  width: 100vw;
  justify-content: center;
  align-items: center;
} 
</style>
