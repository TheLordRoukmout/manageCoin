<script>
    import './app.css';
    import MainMenu from '../components/mainMenu.svelte';
    import ListeCoin from '../components/listeCoin.svelte';
    import { currentTime } from '../lib/time.js';
    import { onMount } from "svelte";
    import axios from 'axios';

    let users = [];
    let coinList = [];
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

        <div class="containerOneTier">

            <div class="container_welcome">

                <div class="name">
                    {#each users as user}
                        <p>Bonjour {user.firstName}</p>
                    {/each}
                </div>

                <div class="info_date">
                    <p>{$currentTime}</p>
                </div>
                
            </div>

            <div class="container_infos">
                <div class="element_infos">
                    <div class="infos">
                        <h4>Wallet actif</h4><br>
                        {#each users as user}
                            <p>{user.wallet.length}</p>
                        {/each}
                    </div>
                    <div class="icon_infos">
                        <span class="material-symbols-outlined">wallet</span>
                    </div>
                </div>
            </div>

            <div class="container_infos">
                <div class="element_infos">
                    <div class="infos">
                    <h4>Associate</h4><br>
                        {#each users as user}
                            <p>{user.associate.length}</p>
                        {/each}
                    </div>
                    <div class="icon_infos">
                        <span class="material-symbols-outlined">group</span>
                    </div>
                </div>
            </div>

            <div class="container_infos">
                <div class="element_infos">
                    <div class="infos">
                        <h4>Percent in last 24h</h4><br>
                        <p>+12,5%</p>
                    </div>
                    <div class="icon_infos">
                        <span class="material-symbols-outlined">show_chart</span>
                    </div>
                </div>
            </div>


        </div>

        <div class="containerSecondTier">

            <div class="listCoin">
                <div class="containerListCoint">
                    <ListeCoin/>
                </div>
                
            </div>
        </div>

    </div>

</main>

<style>
    *{
        display: flex;
    }

    .mainContainer{
        width: 100%;
    }

    .containerOneTier {
        display: flex;
        flex-direction: column;
        width: 33%; /* 100% pour qu'il occupe toute la largeur disponible */
        box-sizing: border-box;
        align-items: center;
        gap: 20px;
    }

    .container_welcome {
        width: 90%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 50px;
        flex-wrap: wrap;
    }

    .name, .info_date {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 40px;
        width: 44%;
        margin-right: 5px;
        margin-left: 5px;
        border-radius: 10px;
        background: linear-gradient(90deg, #2288FF 5%, #C5DFFD 100%);
        font-family: Jaldi, sans-serif;
        color: #fff;
        box-shadow: 3px 3px 5px 0px rgba(0, 0, 0, 0.062);
        max-width: 300px;
        min-width: 150px;
    }

    .container_infos{
        width: 90%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
    }

    .element_infos{
        width: 90%;
        height: 160px;
        border-radius: 10px;
        background: linear-gradient(90deg, #56a4fd 1%, #fbfdff 100%);
        box-shadow: 3px 3px 5px 0px rgba(0, 0, 0, 0.075);
        overflow: hidden;
    }

    .infos{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 50%;
        font-family: Jaldi, sans-serif;
        font-weight: 700;
    }

    .infos h4{
        font-size: 15px;
        margin-top: 10px;
        color: #fff;
    }
    
    .infos p{
        font-size: 50px;
        color: #fff;
    }

    .icon_infos{
        width: 50%;
        display: flex;
        align-items: center;
        justify-content: flex-end;
    }

    .icon_infos span{
        color: #fff;
        opacity: 42%;
        margin-right: -15px;
        font-size: 150px;
    }

    .containerSecondTier{
        width: 33%;
        display: flex;
        justify-content: center;

    }

    .listCoin{
        display: flex;
        justify-content: center;
        margin-top: 110px;
        width: 90%;
        height: 520px;
        border-radius: 10px;
        box-shadow: 3px 3px 5px 0px rgba(0, 0, 0, 0.3);
        background: linear-gradient(260deg, #56a4fd 20%, #d3e8fd 100%);
        overflow: hidden;
        padding: 10px;
        color: rgb(255, 255, 255);
        font-family: Jaldi, sans-serif;
    }

    .containerListCoint{
        overflow: hidden;
        overflow-y: scroll;
        width: 99%;
        height: 99%;
    }
    
    /* chrome, safari */
    .containerListCoint::-webkit-scrollbar {
        display: none;
    }

    /* firefox */
    .containerListCoint {
        scrollbar-width: none;
    }

</style>
