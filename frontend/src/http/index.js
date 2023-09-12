import axios from "axios";

// Настройте базовый URL для вашего сервера Django
axios.defaults.baseURL = 'https://backend-drakonadm.cloud.okteto.net/';
axios.defaults.withCredentials = true; // Включите передачу куков

const $host = axios.create({
    baseURL: process.env.REACT_APP_API_URL
})

const $authHost = axios.create({
    baseURL: process.env.REACT_APP_API_URL,
    withCredentials: true,
})

export {
    $host,
    $authHost
}