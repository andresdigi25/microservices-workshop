import axios from "axios";

export async function login(email, password) {
    try {
        await axios.post(`/api-login/login`, {
            username: email,
            password: password,
        });
        return "success"
    } catch (err) {
        return Promise.reject(err)
    }
}
