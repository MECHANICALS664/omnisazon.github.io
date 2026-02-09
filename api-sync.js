// Updating api-sync.js to use BACKEND_URL from config.js

import { BACKEND_URL } from './config';

const REQUEST_TIMEOUT = 5000; // Setting request timeout

async function fetchData(endpoint) {
    const response = await fetch(`${BACKEND_URL}/${endpoint}`, {
        method: 'GET',
        timeout: REQUEST_TIMEOUT
    });
    return response.json();
}

export { fetchData };