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
  <div id="container">
  <h1>Zip Finder</h1><br/>
  <div>
  <input v-model="zip" id="zip-searcher" />
  <button id="search-button" @click="search">Search</button>
  </div>
  <h1 id="response-message" v-if="displayCityAndState"> The city and state of the entered zip is <br/><span id="location">{{city}},{{state}}</span> </h1>
  </div>
</template>

<style>
h1, button{
  color:white;
  -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: #F36B24;
}
#container{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  background-color: #6EC1E4;
  padding:70px;
  border-radius: 3px;
  border:3px solid grey;
}
#search-button {
  margin-left: 5px;
  cursor: pointer;
}
#zip-searcher {
  margin-top: 5vh;
  width:60vw;
}
#response-message {
  text-align:center;
}
#location {
  border-bottom: 3px solid grey;
}
</style>