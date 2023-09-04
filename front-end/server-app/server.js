const express = require('express');
const cors = require('cors');
const jwt = require('jsonwebtoken'); // JWT 모듈 추가

const app = express();
const PORT = process.env.PORT || 3001;

app.use(express.json());
app.use(cors());

// 비밀 키 (실제 프로덕션 환경에서는 보안에 주의하여 보관해야 함)
const secretKey = 'your-secret-key';

// 로그인 성공 시 세션 키를 발급하는 함수
function issueToken(userId) {
  const payload = { userId };
  const options = { expiresIn: '1h' }; // 세션 키의 유효 기간 설정
  return jwt.sign(payload, secretKey, options);
}

const users = [
  { id: 1, username: 'user1', password: 'password1' },
  { id: 2, username: 'user2', password: 'password2' },
];

app.post('/api/login', (req, res) => {
  const { username, password } = req.body;

  const user = users.find(u => u.username === username && u.password === password);

  if (user) {
    // 로그인 성공 시 세션 키 발급
    const token = issueToken(user.id);
    res.status(200).json({ message: '로그인 성공!', token });
  } else {
    res.status(401).json({ message: '로그인 실패. 사용자 이름 또는 비밀번호가 잘못되었습니다.' });
  }
});

// 홈페이지 접근 시 세션 키 검증 미들웨어
function authenticateToken(req, res, next) {
  const token = req.headers['authorization'];
  if (!token) return res.status(401).json({ message: '세션이 유효하지 않습니다.' });

  jwt.verify(token, secretKey, (err, user) => {
    if (err) return res.status(403).json({ message: '세션이 만료되었습니다.' });
    req.user = user;
    next();
  });
}

app.get('/api/home', authenticateToken, (req, res) => {
  // 세션 키가 유효한 경우에만 홈페이지 보여주기
  res.json({ message: '홈페이지입니다.' });
});

app.listen(PORT, () => {
  console.log(`서버가 포트 ${PORT}에서 실행 중입니다.`);
});
