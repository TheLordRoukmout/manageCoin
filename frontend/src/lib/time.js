// src/lib/time.js
import { writable } from 'svelte/store';

// Créer un store réactif pour l'heure
export const currentTime = writable('');

// Fonction pour mettre à jour l'heure
function updateTime() {
    const now = new Date();
    currentTime.set(now.toLocaleString());  // Mise à jour avec la date et l'heure actuelles
}

// Mettre à jour l'heure toutes les secondes
setInterval(updateTime, 1000);

// Initialisation de l'heure immédiatement
updateTime();
