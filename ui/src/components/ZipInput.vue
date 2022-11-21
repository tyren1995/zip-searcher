<script setup>
import axios from 'axios'
import { ref } from 'vue'

const zip = ref('');
let city= ref('');
let state= ref('');
let displayCityAndState = ref(false);

const search = () => {
if(zip.value.length !== 5){
 return alert('Please enter a valid 5 digit zip code.')
}
else{
return axios.post('http://127.0.0.1:8000/find-zip', {"zip" : zip.value}).then(
  (res)=>(
      city.value = res.data['city'],
      state.value = res.data['state'],
      displayCityAndState.value = true
  )
)
}
};

</script>

<template>
  <h1>Zip Finder</h1><br/>
  <div>
  <input v-model="zip" id="zip-searcher" />
  <button @click="search">Search</button>
  </div>
  <p  v-if="displayCityAndState"> The city and state of the entered zip is {{city}},{{state}} </p>
</template>

<style>
#zip-searcher {
  margin-top: 10vh;
  width:80vw;
}
</style>