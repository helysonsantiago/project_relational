import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Importação dos componentes de roteamento
import Login from '../components/Auth/Login'; // Importação do componente Login
import Home from '../pages/Home'; // Importação do componente Home

const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} /> // Rota para a página de login
        <Route path="/home" element={<Home />} /> // Rota para a página home
      </Routes>
    </Router>
  );
};

export default AppRoutes; // Exportação do componente AppRoutes
