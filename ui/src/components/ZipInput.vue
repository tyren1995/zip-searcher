<template>
  <q-card id="container">
    <q-card-section>
    <q-chip id="logo" size="80px" color="orange" text-color="white"><h1>Zip Finder</h1></q-chip><br/>
    </q-card-section>
    <q-card-section>
  <q-input outlined v-model="zip" id="input" placeholder="Enter Zip Code Here..."  >
  <template v-slot:append>
      <q-icon id="search" @click="queryUSPSAPI" name="search" />
  </template>
  </q-input>
  </q-card-section>
  <br/>
  <q-inner-loading :showing="visible">
      <q-spinner-gears size="100px" color="primary" />
  </q-inner-loading>
  <h1 id="response-message" v-if="displayCityAndState"> 
    The city and state of the entered zip is <br/><span id="location">{{city}},{{state}}</span> 
  </h1>
</q-card>

<q-dialog v-if="displayErrorAlert" v-model="alert">
      <q-card>
        <q-card-section>
          <div class="text-h6">Error</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          Sorry, there has been an error while attempting to contact the server.
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="OK" color="primary" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'

const zip = ref('');
const city= ref('');
const state= ref('');
const displayCityAndState = ref(false);
const displayErrorAlert = ref(true);
const visible = ref(false);

const showLoadingCircle = () => {
        visible.value = true
      };
const hideLoadingCircle = () => {
        visible.value = false
      };

const queryUSPSAPI = () => {
if(zip.value.length !== 5){
 return alert('Please enter a valid 5 digit zip code.')
}
else{
showLoadingCircle();
 try{
  axios.post('http://127.0.0.1:8000/find-zip', {"zip" : zip.value}).then((res)=>{
      hideLoadingCircle();
      return(
      city.value = res.data['city'],
      state.value = res.data['state'],
      displayCityAndState.value = true
      );
})
 }catch(error){
    return displayErrorAlert.value = true
 }

}
};
</script>

<style>
#container{
  text-align: center;
}
#input{
  width:20vw;
}
#logo{
  border-radius: 80px;
}
#search{
  cursor:pointer
}
#response-message {
  text-align:center;
}
#location {
  border-bottom: 3px solid grey;
}
</style>