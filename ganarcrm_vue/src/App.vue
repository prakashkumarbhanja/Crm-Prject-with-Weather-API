<template>
  <div id="nav">
    <Navbar />
    
    <router-view />
    <Loadingpage v-if="this.$store.state.isLoading"/>
  </div>
</template>

<script>
import Navbar from "@/components/layout/Navbar";
import Loadingpage from "@/components/layout/Loadingpage";

import axios from 'axios';

export default {
  name: "App",
  
  components: {
    Navbar,
    Loadingpage,
  },

  beforeCreate() {
    this.$store.commit('initializeStore')

    if(this.$store.state.token){
      axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
    }else{
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
};
</script>


<style lang="scss">

</style>
