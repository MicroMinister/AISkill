<template>
    <div>
      <h1>Register</h1>
      <form @submit.prevent="register">
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit">Register</button>
      </form>
    </div>
  </template>
  
<script>
  export default {
    name: "UserRegister",
    data() {
      return {
        username: "",
        email: "",
        password: "",
      };
    },
    methods: {
      async register() {
        // Replace with your actual registration API endpoint
        const url = "https://your-api-url.com/register";
        try {
          const response = await this.$http.post(url, {
            username: this.username,
            email: this.email,
            password: this.password,
          });
  
          if (response.status === 201) {
            this.$router.push("/login");
          } else {
            alert("Registration failed");
          }
        } catch (error) {
          console.error(error);
        }
      },
    },
  };
</script>
  
<style scoped>
/* Add your styles here */
</style>
  