<script>
    import { onMount } from 'svelte';

    let activeLink = ''; // Variable pour l'URL active

    // Cette fonction s'exécutera après le montage côté client
    onMount(() => {
        // Met à jour activeLink selon l'URL actuelle
        activeLink = window.location.pathname;
    });

    // Fonction pour savoir si le lien est actif
    function setActive(link) {
        activeLink = link; // Met à jour le lien actif
    }
</script>

<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />

<nav class="container_nav">
    <div class="nav_content_top">
        <a href="/" class={activeLink === '/' ? 'active' : ''} on:click={() => setActive('/')}>
            <span class="material-symbols-outlined">home</span>
        </a>
        <a href="/wallet" class={activeLink === '/wallet' ? 'active' : ''} on:click={() => setActive('/wallet')}>
            <span class="material-symbols-outlined">account_balance_wallet</span>
        </a>
        <a href="/count" class={activeLink === '/count' ? 'active' : ''} on:click={() => setActive('/count')}>
            <span class="material-symbols-outlined">monitoring</span>
        </a>
        <a href="/history" class={activeLink === '/history' ? 'active' : ''} on:click={() => setActive('/history')}>
            <span class="material-symbols-outlined">history</span>
        </a>
        <a href="/usersdata" class={activeLink === '/usersdata' ? 'active' : ''} on:click={() => setActive('/usersdata')}>
            <span class="material-symbols-outlined">group</span>
        </a>
    </div>
    <div class="nav_content_bot">
        <a href="/">
            <span class="material-symbols-outlined">notifications</span>
        </a>
        <a href="/">
            <span class="material-symbols-outlined">settings</span>
        </a>
    </div>
</nav>

<slot />

<style>
.container_nav {
    width: 80px;
    height: 100vh; /* Occupe toute la hauteur de la fenêtre */
    background-color: #323232;
    box-shadow: 3px 3px 5px 0px rgba(0,0,0,0.58);
    display: flex;
    flex-direction: column;
    justify-content: space-between; /* Assure une répartition égale de l'espace entre les éléments */
    align-items: center;
    overflow: hidden;
    border-radius: 0 40px 0 0;
}

.nav_content_top {
    display: flex;
    flex-direction: column;
    gap: 20px;
    margin-top: 50px;
    flex-grow: 1; /* Cette section prendra la majeure partie de l'espace */
}

.nav_content_bot {
    display: flex;
    flex-direction: column;
    gap: 20px;
    margin-bottom: 50px;
    margin-top: auto; /* Pousse cette section en bas de l'écran */
}

.nav_content_top a, .nav_content_bot a {
    width: 40px;
    height: 40px;
    background-color: #ffffff71;
    box-shadow: 3px 3px 5px 0px rgba(0,0,0,0.18);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    text-decoration: none;
    color: #fff;
    transition: background-color 0.3s ease;
}

.nav_content_top a:hover, .nav_content_bot a:hover {
    background-color: #A3F23E;
}

.nav_content_top a.active, .nav_content_bot a.active {
    background-color: #A3F23E; /* Lien actif */
    color: white;
}

</style>
