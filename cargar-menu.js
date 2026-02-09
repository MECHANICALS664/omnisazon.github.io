// ==================== CARGAR MENÚ (INTENTA BACKEND → FALLBACK menu.json) ====================
// Nota: BACKEND_URL se carga desde config.js

let platillosDelBackend = []; // Guardar platillos cargados

async function cargarMenuDesdeBackend() {
    // Intentar backend primero (desarrollo)
    try {
        console.log('📦 Intentando cargar menú desde backend...');
        const response = await fetch(`${BACKEND_URL}/api/menu`, { cache: 'no-store' });
        if (response.ok) {
            const result = await response.json();
            if (result && result.success && Array.isArray(result.data)) {
                platillosDelBackend = result.data;
                mostrarMenuDeLaBD(result.data);
                console.log('✅ Menú cargado desde backend:', result.data.length, 'platillos');
                return;
            }
        }
        console.warn('⚠️ Backend no respondió con datos válidos, intentando menu.json...');
    } catch (err) {
        console.warn('⚠️ No se pudo conectar al backend:', err);
    }

    // Fallback: cargar frontend/menu.json (útil para GitHub Pages)
    try {
        console.log('📦 Cargando menú desde frontend/menu.json...');
        const resp = await fetch('menu.json', { cache: 'no-store' });
        if (!resp.ok) throw new Error('menu.json no disponible');
        const json = await resp.json();
        if (json && (Array.isArray(json) || (json.success && Array.isArray(json.data)))) {
            const data = Array.isArray(json) ? json : json.data;
            platillosDelBackend = data;
            mostrarMenuDeLaBD(data);
            console.log('✅ Menú cargado desde menu.json:', data.length, 'platillos');
            return;
        }
        throw new Error('Formato inválido en menu.json');
    } catch (err) {
        console.error('❌ Error cargando menu.json:', err);
        mostrarMensajeError('No se pudo cargar el menú');
    }
}

function mostrarMenuDeLaBD(platillos) {
    const menuGrid = document.getElementById('menuGrid');
    
    if (!menuGrid) {
        console.error('❌ No se encontró el elemento #menuGrid');
        return;
    }
    
    menuGrid.innerHTML = '';
    
    platillos.forEach(platillo => {
        // Capitalizar la primera letra del nombre
        const nombreCapitalizado = platillo.nombre.trim().charAt(0).toUpperCase() + platillo.nombre.trim().slice(1).toLowerCase();
        
        const menuItem = document.createElement('div');
        menuItem.className = 'menu-item';
        menuItem.innerHTML = `
            <div>
                <h3>${nombreCapitalizado}</h3>
                <p class="precio">$${platillo.precio.toFixed(2)}</p>
            </div>
            <button class="add-btn" onclick="addToOrder(${platillo.id}, this)">
                ➕ Agregar
            </button>
        `;
        menuGrid.appendChild(menuItem);
    });
}

function mostrarMensajeError(mensaje) {
    const menuGrid = document.getElementById('menuGrid');
    if (menuGrid) {
        menuGrid.innerHTML = `<p style="grid-column: 1/-1; color: red; text-align: center;">${mensaje}</p>`;
    }
}

// Cargar menú cuando carga la página
document.addEventListener('DOMContentLoaded', cargarMenuDesdeBackend);
