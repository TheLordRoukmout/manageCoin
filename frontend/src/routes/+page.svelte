<script>
    import './app.css';
    import MainMenu from '../components/mainMenu.svelte';
</script>

<main>
    <MainMenu/>
    <div class="mainContainer">
        <h1>Test</h1>
    </div>
</main>

<style>
    *{
        display: flex;
    }

    .mainContainer{
        background-color: wheat;
        width: 100%;
    }

</style>
