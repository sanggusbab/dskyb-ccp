// LoginForm.js
import React, { useState } from 'react';
import { loginUser, login } from '../../api'; // api.js에서 loginUser와 login 함수 가져오기
import { useNavigate } from 'react-router-dom'; // useNavigate를 import로 변경

function LoginForm() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate(); // useNavigate를 사용하여 네비게이션 설정

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await loginUser(username, password); // loginUser 함수 사용
            alert(response.message);
            // 로그인 성공 후 필요한 작업 수행
            // 예: 홈페이지로 리다이렉트
            navigate('/home'); // '/home' 경로로 리다이렉트
        } catch (error) {
            console.error('로그인 요청 중 오류 발생:', error);
            alert('로그인 실패. 사용자 이름 또는 비밀번호가 잘못되었습니다.');
        }
    };
    return (
        <div>
            <h2>로그인</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="username">사용자 이름:</label>
                    <input
                        type="text"
                        id="username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="password">비밀번호:</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">로그인</button>
            </form>
        </div>
    );
}

export default LoginForm;