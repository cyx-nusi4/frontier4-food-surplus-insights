<template>
  <div id="app">
    <nav>
      <router-link to="/food">Food</router-link>
      <router-link to="/dss">DSS</router-link>
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
}

nav {
  display: flex;
  justify-content: center;
  gap: 20px;
  padding: 10px;
  background-color: #f4f4f4;
  border-bottom: 1px solid #ddd;
}

nav a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

nav a.router-link-active {
  color: #007bff;
}
</style>