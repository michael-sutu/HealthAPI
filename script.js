if(localStorage.getItem("userid") == null) {
    document.getElementById("noauth").style.display = "block"
} else {
    fetch("/get?userid="+localStorage.getItem("userid"))
        .then(response => response.json())
        .then(data => {
            if(data) {
                document.getElementById("auth").style.display = "block"
                document.getElementById("callsDisplay").textContent = "API Calls: "+data.Calls
                document.getElementById("keyDisplay").textContent = "API Key:  "+data.Key
            } else {
                localStorage.removeItem("userid")
                location.reload()
            }
        })
}

document.getElementById("loginBtn").addEventListener("click", (e) => {
    fetch(`/login?username=${document.getElementById("usernameInput").value}&password=${document.getElementById("passwordInput").value}`)
        .then(response => response.json())
        .then(data => {
            if(data) {
                localStorage.setItem("userid", data)
                location.reload()
            } else {
                alert("Unable to login to account.")
            }
        })
})

document.getElementById("signupBtn").addEventListener("click", (e) => {
    fetch(`/signup?username=${document.getElementById("usernameInput").value}&password=${document.getElementById("passwordInput").value}`)
        .then(response => response.json())
        .then(data => {
            if(data) {
                localStorage.setItem("userid", data)
                location.reload()
            } else {
                alert("Unable to create account.")
            }
        })
})

document.getElementById("logoutBtn").addEventListener("click", (e) => {
    localStorage.removeItem("userid")
    location.reload()
})