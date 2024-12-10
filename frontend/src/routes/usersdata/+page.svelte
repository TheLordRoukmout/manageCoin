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
  <h1>Liste des utilisateurs</h1>

  {#if loading}

    <p>Chargement des données...</p>
    
  {:else}

    <ul>

      {#each users as user}
        <p>Bonjour {user.firstName}</p>
      {/each}

    </ul>
    
  {/if}



</main>

<style>
    *{
        display: flex;
    }
</style>
