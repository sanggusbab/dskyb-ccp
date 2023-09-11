import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // 'Routes' 추가

import LoginForm from './components/LoginForm/LoginForm';
import Home from './pages/Home';
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes> {/* 'Routes'로 변경 */}
          <Route path="/home" element={<Home />} /> {/* 'element'를 사용하여 컴포넌트를 렌더링 */}
          <Route path="/login" element={<LoginForm />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
