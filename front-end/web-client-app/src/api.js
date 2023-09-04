// api.js
import axios from 'axios';
export const loginUser = async (username, password) => {
    try {
        const response = await fetch('http://localhost:3001/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });

        if (response.ok) {
            const data = await response.json();
            return data;
        } else {
            const data = await response.json();
            return data;
        }
    } catch (error) {
        console.error('로그인 요청 중 오류 발생:', error);
        throw error;
    }
};

// 로그인 후 JWT를 저장
function login(username, password) {
    return axios.post('http://localhost:3001/api/login', { username, password })
        .then(response => {
            const { token } = response.data;
            localStorage.setItem('token', token); // 로컬 스토리지에 토큰 저장
        });
}

// 홈페이지 접근 (JWT를 헤더에 추가)
function getHomePage() {
    const token = localStorage.getItem('token'); // 저장된 토큰 가져오기

    if (!token) {
        return Promise.reject('세션이 유효하지 않습니다.');
    }

    const headers = {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
    };

    return axios.get('http://localhost:3001/api/home', { headers })
        .then(response => response.data)
        .catch(error => {
            if (error.response.status === 403) {
                return Promise.reject('세션이 만료되었습니다.');
            } else {
                return Promise.reject('세션이 유효하지 않습니다.');
            }
        });
}

// 로그아웃 (토큰 삭제)
function logout() {
    localStorage.removeItem('token'); // 로컬 스토리지에서 토큰 삭제
}

export { login, getHomePage, logout };
