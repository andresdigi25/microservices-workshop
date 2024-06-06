import axios from "axios";

export async function login(email, password) {
    try {
        /*await axios.post(`/api/auth/login/`, {
            username: email,
            password: password,
        });*/
        return new Promise(resolve => {
            setTimeout(() => {
                resolve("success")
            }, 1000)
        })
    } catch (err) {
        return Promise.reject(err)
    }
}
