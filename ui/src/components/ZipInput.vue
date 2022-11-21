<script setup>
import axios from 'axios'
import { ref } from 'vue'

const zip = ref('');
let city= ref('');
let state= ref('');
let displayCityAndState = ref(false);

const queryUSPSAPI = () => {
if(zip.value.length !== 5){
 return alert('Please enter a valid 5 digit zip code.')
}
else{
return axios.post('http://127.0.0.1:8000/find-zip', {"zip" : zip.value}).then((res)=>(
      city.value = res.data['city'],
      state.value = res.data['state'],
      displayCityAndState.value = true
  ))
}
};
</script>

<template>
  <div id="container">
  <h1>Zip Finder</h1><br/>
  <input v-model="zip" placeholder="Enter Zip Code Here..." id="zip-input" /><br/>
  <button id="search-button" @click="queryUSPSAPI">Search</button>
  <h1 id="response-message" v-if="displayCityAndState"> 
    The city and state of the entered zip is <br/><span id="location">{{city}},{{state}}</span> 
  </h1>
  </div>
</template>

<style>
h1{
  color:white;
  -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: #F36B24;
}
input:focus {
    outline: none !important;
    border:1px solid grey;
  }
#container{
  display: flex;
  width:80vw;
  height:40vh;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #6EC1E4;
  padding:30px;
  border-radius: 3px;
  border:2px solid grey;
}
#search-button {
  background-color: #F36B24;
  color: white;
  border-radius: 3px;
  border: 1px solid black;
  margin-left: 5px;
  width:15vw;
  height:30px;
  cursor: pointer;
}
#zip-input {
  text-align: center; 
  border-radius: 3px;
  width:30vw;
  height:25px;
}
#response-message {
  text-align:center;
}
#location {
  border-bottom: 3px solid grey;
}
</style>