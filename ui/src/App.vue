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
  flex-direction: column;
  height: 60vh;
  width: 100vw;
  justify-content: center;
  align-items: center;
} 
</style>
