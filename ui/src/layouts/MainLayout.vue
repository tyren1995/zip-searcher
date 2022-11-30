<template>
  <q-layout >
    <q-header elevated>
      <q-toolbar class="bg-cyan text-white">
        <q-toolbar-title>
          Zip Searcher
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'MainLayout',

  components: {
    
  },

  setup () {

    return {
    }
  }
})
</script>

