const wrapper = document.querySelector(".wrapper");
const loginLink = document.querySelector(".login-link");
const registerLink = document.querySelector(".register-link");
const loginButton = document.getElementById("login-btn");
const login = document.getElementById("login");
const password = document.getElementById("password");
const registerButton = document.getElementById("register-btn");
const passwordFirst = document.getElementById("password-first");
const passwordSecond = document.getElementById("password-second");
const userName = document.getElementById("username");
const email = document.getElementById("email");
const errorContainer = document.getElementById("password-error");
const loginContainer = document.getElementById("login-error");

localStorage.setItem('ip', 'localhost');
const ip = localStorage.getItem('ip');

registerLink.addEventListener('click', ()=>{
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', ()=>{
    wrapper.classList.remove('active');
});

loginButton.addEventListener('click', () => {
    window.location.href='main.html';
    const loginValue = login.value;
    const passwordValue = password.value;

    const loginUrl = `http://${ip}:5285/Home/Login?login=${encodeURIComponent(loginValue)}&password=${encodeURIComponent(passwordValue)}`;

    fetch(loginUrl, {
        method: 'GET'
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Ошибка при входе');
            }
        })
        .then(data => {
            localStorage.setItem('userId', data.userId);
            localStorage.setItem('token', data.token);
            window.location.href='main.html';
        })
        .catch(error => {
            console.error('Ошибка:', error);
            loginContainer.textContent = "Произошла ошибка";
        });
});

registerButton.addEventListener('click', () => {
    const passwordFirstValue = passwordFirst.value;
    const passwordSecondValue = passwordSecond.value;
    const userNameValue = userName.value;
    const emailValue = email.value;

    if(passwordFirstValue === "" || userNameValue === "" || emailValue === ""){
        errorContainer.textContent = "Заполните все поля";
    }
    else if (passwordFirstValue === passwordSecondValue) {
        const formData = new FormData();
        formData.append('login', userNameValue);
        formData.append('email', emailValue);
        formData.append('password', passwordFirstValue);
        fetch('http://'+ ip +':5285/Home/Register', {
            method: 'PUT',
            body: formData
        })
            .then(response => {
                if (response.ok) {
                    errorContainer.textContent = "Регистрация прошла успешно";
                } else {
                    errorContainer.textContent = "Ошибка при регистрации";
                }
            })
            .catch(error => {
                console.error('Ошибка:', error);
                errorContainer.textContent = "Произошла ошибка";
            });
    }
    else {
        errorContainer.textContent = "Пароли не совпадают";
    }
});
