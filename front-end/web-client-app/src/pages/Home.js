// Home.js
import React, { useEffect, useState } from 'react';
import { getHomePage } from '../api'; // api.js에서 getHomePage 함수 가져오기

function Home() {
    const [content, setContent] = useState(null);

    useEffect(() => {
        fetchHomePageContent();
    }, []);

    const fetchHomePageContent = async () => {
        try {
            const data = await getHomePage();
            setContent(data.message);
        } catch (error) {
            console.error('홈페이지 데이터 가져오기 실패:', error);
            // 사용자에게 에러 메시지를 표시하거나 다른 조치를 취할 수 있음
        }
    };

    return (
        <div>
            <h2>홈페이지</h2>
            {content ? (
                <div>{content}</div>
            ) : (
                <p>로딩 중...</p>
            )}
        </div>
    );
}

export default Home;