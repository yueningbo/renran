import Vue from 'vue'
import Router from 'vue-router'

import Home from "../components/Home"
import Login from "../components/Login"

Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    //路由列表
    {
      name: "Home",
      path: "/",
      component: Home,
    },
    {
      name: "Home",
      path: "/home",
      component: Home,
    },
    {
      name: "Login",
      path: "/user/login",
      component: Login,
    },
  ]
})
