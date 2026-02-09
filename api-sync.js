// ==================== SINCRONIZACIÓN DE PEDIDOS CON BACKEND ====================
// Este archivo maneja la comunicación de pedidos entre el mesero y la cocina

class OrderSync {
    constructor() {
        this.syncInterval = null;
        this.isSyncing = false;
        this.lastSyncTime = 0;
        this.syncDelay = 1000; // Sincronizar cada 1 segundo
    }

    /**
     * Enviar pedido al backend (para mesero -> cocina)
     */
    async sendOrderToBackend(orderData) {
        try {
            console.log('📤 Enviando pedido al backend:', orderData);
            
            const response = await fetch(`${BACKEND_URL}/api/pedidos`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(orderData),
                timeout: REQUEST_TIMEOUT
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            const result = await response.json();
            console.log('✅ Pedido recibido por backend:', result);
            
            // También guardar en localStorage como backup
            this.saveOrderLocally(orderData);
            
            return { success: true, data: result };
        } catch (error) {
            console.warn('⚠️ No se pudo enviar al backend, guardando localmente:', error);
            // Fallback: guardar solo en localStorage
            this.saveOrderLocally(orderData);
            return { success: false, error: error.message, savedLocally: true };
        }
    }

    /**
     * Obtener pedidos pendientes del backend (para cocinero)
     */
    async getKitchenOrders() {
        try {
            console.log('📥 Obteniendo pedidos de cocina desde backend...');
            
            const response = await fetch(`${BACKEND_URL}/api/pedidos/cocina`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
                timeout: REQUEST_TIMEOUT
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            const result = await response.json();
            console.log('✅ Pedidos obtenidos del backend:', result);
            return result.data || [];
        } catch (error) {
            console.warn('⚠️ No se pudo obtener pedidos del backend:', error);
            // Fallback: obtener de localStorage
            return this.getOrdersLocally();
        }
    }

    /**
     * Actualizar estado de un pedido en el backend
     */
    async updateOrderStatus(orderId, status) {
        try {
            console.log(`📝 Actualizando pedido ${orderId} a estado: ${status}`);
            
            const response = await fetch(`${BACKEND_URL}/api/pedidos/${orderId}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ status }),
                timeout: REQUEST_TIMEOUT
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            const result = await response.json();
            console.log('✅ Estado actualizado:', result);
            return { success: true, data: result };
        } catch (error) {
            console.warn('⚠️ No se pudo actualizar en backend:', error);
            return { success: false, error: error.message };
        }
    }

    /**
     * Guardar pedido en localStorage como backup
     */
    saveOrderLocally(orderData) {
        try {
            const orders = JSON.parse(localStorage.getItem('kitchenOrders') || '[]');
            
            const orderWithId = {
                ...orderData,
                id: orderData.id || Date.now(),
                synced: false,
                timestamp: new Date().toISOString()
            };
            
            orders.push(orderWithId);
            localStorage.setItem('kitchenOrders', JSON.stringify(orders));
            console.log('💾 Pedido guardado en localStorage');
        } catch (error) {
            console.error('Error guardando en localStorage:', error);
        }
    }

    /**
     * Obtener pedidos de localStorage
     */
    getOrdersLocally() {
        try {
            return JSON.parse(localStorage.getItem('kitchenOrders') || '[]');
        } catch (error) {
            console.error('Error leyendo de localStorage:', error);
            return [];
        }
    }

    /**
     * Iniciar sincronización automática (para cocinero)
     */
    startAutoSync(callback) {
        if (this.syncInterval) return; // Ya está sincronizando
        
        console.log('🔄 Iniciando sincronización automática...');
        
        // Primera sincronización inmediata
        this.syncKitchenOrders(callback);
        
        // Luego, cada X segundos
        this.syncInterval = setInterval(() => {
            this.syncKitchenOrders(callback);
        }, this.syncDelay);
    }

    /**
     * Detener sincronización automática
     */
    stopAutoSync() {
        if (this.syncInterval) {
            clearInterval(this.syncInterval);
            this.syncInterval = null;
            console.log('⏹️ Sincronización detenida');
        }
    }

    /**
     * Sincronizar pedidos de cocina
     */
    async syncKitchenOrders(callback) {
        if (this.isSyncing) return;
        
        this.isSyncing = true;
        try {
            const orders = await this.getKitchenOrders();
            if (callback && typeof callback === 'function') {
                callback(orders);
            }
            this.lastSyncTime = Date.now();
        } catch (error) {
            console.error('Error en sincronización:', error);
        } finally {
            this.isSyncing = false;
        }
    }

    /**
     * Verificar conectividad al backend
     */
    async checkBackendConnection() {
        try {
            const response = await fetch(`${BACKEND_URL}/`, {
                method: 'GET',
                timeout: 3000
            });
            return response.ok;
        } catch (error) {
            console.warn('No hay conexión con backend:', error);
            return false;
        }
    }
}

// Instancia global del sincronizador
const orderSync = new OrderSync();

// Log de inicialización
console.log('✅ API Sync initialized - Ready to sync orders');
