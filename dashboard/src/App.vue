<template>
  <div id="app">
    <nav>
      <router-link to="/food">Food Surplus Overview</router-link>
      <router-link to="/dss">DSS Overview</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
  font-family: Arial, sans-serif;
  background-color: #d4f7d4; /* light green */
}

nav {
  display: flex;
  justify-content: center;
  gap: 20px;
  padding: 10px;
  background-color: #145a32; /* dark green */
  border-bottom: 1px solid #ddd;
  font-family: Arial, sans-serif;
}

nav a {
  text-decoration: none;
  color: #fff;
  font-weight: bold;
  font-family: Arial, sans-serif;
}

nav a.router-link-active {
  color: #ffeb3b;
  font-family: Arial, sans-serif;
}
</style>