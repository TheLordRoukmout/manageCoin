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
                        <h4 >Wallet actif</h4><br>
                        {#each users as user}
                            <p >{user.wallet.length}</p>
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

            <div class="container_infos_percent">
                <div class="element_infos_percent">
                    <div class="infos_percent">
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

        <div class="containerThirdTier">
            
            <div class="container_fav">

                <div class="element_fav">

                    <div class="icon_fav">
                        <span class="material-symbols-outlined">currency_bitcoin</span>
                    </div>
                    <div class="infos_fav">
                        <p >99 974.02 $</p>
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
        font-family: Jaldi, sans-serif;
        color: #fff;
        box-shadow: 3px 3px 5px 0px rgba(0, 0, 0, 0.062);
        max-width: 300px;
        min-width: 150px;
    }

    .name{
        background-color: #A3F23E;
        font-size: 20px;
    }

    .info_date{
        background-color: #323132;
    }

    .container_infos{
        width: 90%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        cursor: pointer;
        transition: transform 0.3s ease;
    }

    .container_infos:hover{
        transform: scale(1.03);
    }

    .element_infos{
        width: 90%;
        height: 160px;
        border-radius: 10px;
        background-color: #323232;
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
        color: #A3F23E;
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

    .container_infos_percent{
        width: 90%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        cursor: pointer;
        transition: transform 0.3s ease;
    }

    .container_infos_percent:hover{
        transform: scale(1.03);
    }

    .element_infos_percent{
        width: 90%;
        height: 160px;
        border-radius: 10px;
        border: 1px solid #A3F23E;
        background: linear-gradient(135deg, hsla(0, 0%, 20%, 1) 12%, hsla(86, 87%, 60%, 1) 87%);
        box-shadow: 3px 3px 5px 0px rgba(0, 0, 0, 0.075);
        overflow: hidden;
        
    }

    .infos_percent{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 50%;
        font-family: Jaldi, sans-serif;
        font-weight: 700;
        
    }

    .infos_percent h4{
        font-size: 15px;
        margin-top: 10px;
        color: #fff;
    }

    .infos_percent p{
        font-size: 50px;
        color: #ffffff;
    }

    .containerSecondTier{
        width: 33%;
        display: flex;
        justify-content: center;

    }

    .listCoin{
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 110px;
        width: 90%;
        height: 520px;
        border-radius: 10px;
        box-shadow: 3px 3px 5px 0px rgba(0, 0, 0, 0.3);
        background-color: #323232;
        overflow: hidden;
        padding: 10px;
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

    .containerThirdTier{
        display: flex;
        justify-content: center;
        width: 33%;
        height: 100vh;
    }
    .container_fav{
        display: flex;
        flex-direction: column;
        width: 90%;
        
    }

    .element_fav{
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 110px;
        width: 90%;
        height: 100px;
        border-radius: 10px;
        background: linear-gradient(98deg, hsla(0, 0%, 20%, 1) 2%, hsla(86, 87%, 60%, 1) 87%);
        border: 1px solid #A3F23E;
        box-shadow: 3px 3px 5px 0px rgba(0, 0, 0, 0.3);
        overflow: hidden;
        
    }

    .icon_fav{
        display: flex;
        align-items: end;
        justify-content: center;
        width: 20%;
    }

    .material-symbols-outlined{
        font-size: 50px;
        color: #fff;
        margin-right: 80%;
    }

    .infos_fav{
        display: flex;
        align-items: center;
        font-size: 50px;
        font-family: Jaldi, sans-serif;
        color: #fff;
    }

</style>
