<script>
    import MainMenu from "../../components/mainMenu.svelte";
    import ListeCoin from "../../components/listeCoin.svelte";

</script>

<main>
    
    <MainMenu/>
    <div class="mainContainer">
        <ListeCoin/>
    </div>
 
</main>

<style>
    
    *{
        display: flex;
    }

    .mainContainer{
        width: 100%;
        height: 100vh;
        overflow: hidden;
        overflow: scroll;
    }

</style>
