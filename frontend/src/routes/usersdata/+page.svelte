<script>
  
  import { onMount } from "svelte";
  import axios from 'axios';

  let users = []
  let loading = true;

  onMount(async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/api/users');
      users = response.data.users;
    }catch (error){
      console.log("Erreur lors de la récupération des utilisateurs.", error);
    }finally {
      loading = false;
    }
  })

</script>

<main>
  <h1>Liste des utilisateurs</h1>

  {#if loading}

    <p>Chargement des données...</p>
    
  {:else}

    <ul>

      {#each users as user}
        <li>
          {user.firstName} {user.lastName} {user.email}
        </li>
      {/each}

    </ul>
    
  {/if}



</main>

<style>

</style>
