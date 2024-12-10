<script>
    import MainMenu from "../../components/mainMenu.svelte";
    import { onMount } from "svelte";
    import axios from 'axios';

    let users = []
    let loading = true;

    onMount(async () => {
        try {
        const response = await axios.get('http://127.0.0.1:5000/api/users');
        users = response.data;
        }catch (error){
        console.log("Erreur lors de la récupération des utilisateurs.", error);
        }finally {
        loading = false;
        }
    })
</script>

<main>
    <MainMenu/>
    <div class="mainContainer">
        <h1>Wallet</h1>
        <ul>
            {#each users as user}
                {#each user.coinCollection as {coin, quantity}}
                    <li>{coin}: {quantity}</li>
                {/each}
            {/each}
        </ul>
    </div>
</main>

<style>

    *{
        display: flex;
    }

    .mainContainer{
        width: 100%;
    }
</style>