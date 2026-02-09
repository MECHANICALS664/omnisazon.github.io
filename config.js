// ==================== CONFIGURACIÓN DE BACKEND ====================
// Detectar automáticamente si estamos en desarrollo local o producción
const isLocalhost = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';

// URL del backend
const BACKEND_URL = isLocalhost 
    ? 'http://localhost:5000'  // Local development
    : 'https://tu-backend-online.com';  // Cambiar a tu URL de producción cuando despliegues

// Configuración de timeout para requests
const REQUEST_TIMEOUT = 5000; // 5 segundos

// Log de configuración (solo en desarrollo)
if (isLocalhost) {
    console.log('🔧 Configuración en MODO LOCAL');
    console.log('BACKEND_URL:', BACKEND_URL);
} else {
    console.log('🔧 Configuración en MODO PRODUCCIÓN');
    console.log('BACKEND_URL:', BACKEND_URL);
}
