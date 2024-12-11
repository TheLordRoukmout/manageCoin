<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />

<nav class="container_nav">
    <div class="nav_content_top">
        <a href="/" title="home">
            <span class="material-symbols-outlined">home</span>
        </a>
        <a href="/wallet" title="Wallet">
            <span class="material-symbols-outlined">account_balance_wallet</span>
        </a>
        <a href="/count" title="Count">
            <span class="material-symbols-outlined">monitoring</span>
        </a>
        <a href="/history" title="history">
            <span class="material-symbols-outlined">history</span>
        </a>
        <a href="/usersdata" title="associate">
            <span class="material-symbols-outlined">group</span>
        </a>
        <!-- <a href="/about">About</a> -->
        <!-- <a href="/usersdata">Users</a> -->
    </div>
    <div class="nav_content_bot">
        <a href="/" title="notification">
            <span class="material-symbols-outlined">notifications</span>
        </a>
        <a href="/" title="setting">
            <span class="material-symbols-outlined">settings</span>
        </a>
    </div>
</nav>
<slot />

<style>
.container_nav {
    width: 80px;
    height: 100vh; /* Occupe toute la hauteur de la fenêtre */
    background: linear-gradient(90deg, #2288FF 20%, #C5DFFD 100%);
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
}

.nav_content_top a:hover, .nav_content_bot a:hover {
    transition: 0.2s;
    box-shadow: 3px 3px 5px 0px rgba(0,0,0,0.58);
}

.nav_content_top span, .nav_content_bot span {
    color: rgb(255, 255, 255);
}

</style>