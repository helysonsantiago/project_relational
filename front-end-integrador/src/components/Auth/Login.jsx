import { useState } from 'react'; // Hook para gerenciar estado
import { useNavigate } from 'react-router-dom'; // Hook para navegação
import { toast } from 'react-toastify'; // Biblioteca para notificações
import 'react-toastify/dist/ReactToastify.css'; // Estilos para as notificações
import { FaEye, FaEyeSlash } from 'react-icons/fa'; // Ícones para mostrar/ocultar senha

const Login = () => {
  // Estados para armazenar email, senha, visibilidade da senha e opção "Lembrar de mim"
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [rememberMe, setRememberMe] = useState(false);

  // Hook para navegação
  const navigate = useNavigate();

  // Função para lidar com o login
  const handleLogin = (e) => {
    e.preventDefault();
    if (email === 'user@example.com' && password === 'kauan') {
      toast.success('Login bem-sucedido!'); // Notificação de sucesso
      navigate('/home'); // Navega para a página inicial
    } else {
      toast.error('Email ou senha inválidos'); // Notificação de erro
    }
  };

  // Função para lidar com esquecimento de senha
  const handleForgotPassword = () => {
    toast.info('Um link de recuperação de senha foi enviado para seu email.'); // Notificação de informação
  };

  // Função para alternar visibilidade da senha
  const toggleShowPassword = () => {
    setShowPassword(!showPassword);
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <h2>Login</h2>
        <form onSubmit={handleLogin}>
          <div className="form-group">
            <label>Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="form-group password-group">
            <label>Senha</label>
            <div className="password-input">
              <input
                type={showPassword ? 'text' : 'password'}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
              <button type="button" className="toggle-password" onClick={toggleShowPassword}>
                {showPassword ? <FaEyeSlash /> : <FaEye />}
              </button>
            </div>
          </div>
          <div className="form-group checkbox-group">
            <input
              type="checkbox"
              id="rememberMe"
              checked={rememberMe}
              onChange={(e) => setRememberMe(e.target.checked)}
            />
            <label htmlFor="rememberMe">Lembrar de mim</label>
          </div>
          <button type="submit" className="login-button">Entrar</button>
        </form>
        <button onClick={handleForgotPassword} className="forgot-password-button">Esqueci minha senha</button>
      </div>
    </div>
  );
};

export default Login;
