<template>
  <div>
    <p>Home page</p>
    <p>{{randomNumber}}</p>
    <button @click="getRandom">Get Random</button>
  </div>
</template>
<script>
import axios from 'axios'
export default{

  data () {
    return {
      randomNumber: 0
    }
  },
  methods: {
    getRandom () {
      const path = `http://localhost:5000/api/random`
      axios.get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
