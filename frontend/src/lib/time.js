// src/lib/time.js
import { writable } from 'svelte/store';

export const currentTime = writable('');

function updateTime() {
    const now = new Date();
    currentTime.set(now.toLocaleString());  // Mise à jour avec la date et l'heure actuelles
}

setInterval(updateTime, 1000);

updateTime();
