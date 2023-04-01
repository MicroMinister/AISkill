<template>
    <div>
      <h1>Login</h1>
      <form @submit.prevent="login">
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
<script>
  export default {
    name: "UserLogin",
    data() {
      return {
        username: "",
        password: "",
      };
    },
    methods: {
      async login() {
        // Replace with your actual login API endpoint
        const url = "https://your-api-url.com/login";
        try {
          const response = await this.$http.post(url, {
            username: this.username,
            password: this.password,
          });
  
          if (response.status === 200) {
            // Save user authentication data (e.g. token) and redirect to a protected route
            // This is just an example, you should handle the authentication data based on your API response
            localStorage.setItem("authToken", response.data.token);
            this.$router.push("/protected-route");
          } else {
            alert("Login failed");
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
  