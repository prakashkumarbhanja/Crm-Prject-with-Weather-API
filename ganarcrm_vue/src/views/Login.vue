<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log in</h1>
            
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" name="email" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'LogIn',
        data() {
            return {
                username: '',
                password: '',
                errors: []
            }
        },
        methods: {
           async submitForm() {
                console.log("1- Function strated...")

                this.$store.commit('setIsLoading', true)

                console.log("2- setIsLoading is True Now...")

                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')
                const formData = {
                    username: this.username,
                    password: this.password
                }
                console.log("3- Authorization is blank, token is blan and form data created")

               
                    console.log("Login executing")
                await axios
                    .post('/api/v1/token/login/', formData)
                    .then(response => {
                        const token = response.data.auth_token
                        this.$store.commit('setToken', token)
                        axios.defaults.headers.common['Authorization'] = 'Token ' + token
                        localStorage.setItem('token', token)

                        this.$router.push('/dashboard/my-account')

                        console.log("4- Login successfully done...")
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again!')
                        }
                    })
                    
                    console.log("me executing")
                 await axios
                    .get('/api/v1/users/me')
                    .then(response => {
                        // this.$store.commit('setUser', {'id': response.data.id, 'username': response.data.username})
                        localStorage.setItem('username', response.data.username)
                        localStorage.setItem('userid', response.data.id)

                        console.log("5- username and userID sate...")
                    })
                    .catch(error => {
                        console.log("Error on me.")
                        console.log(error)
                    })
                // await axios
                //     .get('/api/v1/teams/get_my_team/')
                //     .then(response => {
                //         console.log(response.data)
                //         this.$store.commit('setTeam', {
                //             'id': response.data.id, 
                //             'name': response.data.name,
                //             'plan': response.data.plan.name,
                //             'max_leads': response.data.plan.max_leads,
                //             'max_clients': response.data.plan.max_clients
                //         })
                //         this.$router.push('/dashboard/my-account')
                //     })
                //     .catch(error => {
                //         console.log(error)
                //     })
                console.log("6- setIsLoading is now False...")
                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>