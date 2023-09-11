import React, { useState, useEffect } from 'react';
import { loginUser, login, getHomePage } from '../../api'; // api.js에서 loginUser와 login 함수 가져오기
import { useNavigate } from 'react-router-dom'; // useNavigate를 import로 변경

function LoginForm() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [isLoggedIn, setIsLoggedIn] = useState(false); // 로그인 상태를 추적
    const navigate = useNavigate(); // useNavigate를 사용하여 네비게이션 설정

    // 컴포넌트가 마운트될 때 로그인 상태를 확인하고 세션 키가 있는 경우 로그인 상태로 설정
    useEffect(() => {
        const token = localStorage.getItem('token');
        if (token) {
            setIsLoggedIn(true);
        }
    }, []);

    const handleLogin = async () => {
        try {
            const response = await loginUser(username, password); // loginUser 함수 사용
            alert(response.message);

            // 로그인 성공 시 필요한 작업 수행
            if (response.token) {
                localStorage.setItem('token', response.token); // 세션 키 저장
                setIsLoggedIn(true); // 로그인 상태로 설정
                navigate('/home'); // '/home' 경로로 리다이렉트
            }
        } catch (error) {
            console.error('로그인 요청 중 오류 발생:', error);
            alert('로그인 실패. 사용자 이름 또는 비밀번호가 잘못되었습니다.');
        }
    };

    const handleLogout = () => {
        localStorage.removeItem('token'); // 세션 키 삭제
        setIsLoggedIn(false); // 로그아웃 상태로 설정
        navigate('/login'); // '/login' 경로로 리다이렉트
    };

    // 세션 키가 있는 경우 로그아웃 버튼을 보여줌
    const renderLogoutButton = () => {
        if (isLoggedIn) {
            return (
                <button type="button" onClick={handleLogout}>
                    로그아웃
                </button>
            );
        }
        return null;
    };

    return (
        <div>
            <h2>로그인</h2>
            {renderLogoutButton()}
            {isLoggedIn ? (
                <p>로그인 상태입니다.</p>
            ) : (
                <form onSubmit={handleLogin}>
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
            )}
        </div>
    );
}

export default LoginForm;
