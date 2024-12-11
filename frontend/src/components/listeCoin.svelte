<script>
    import { onMount } from "svelte";
    import axios from 'axios';

    let coinList = [];
    let loading = true;

    onMount(async () => {
        try {
            const response = await axios.get('http://127.0.0.1:5000/api/coinlist');
            coinList = response.data.data;  // Accède à `data` pour obtenir la liste des coins
        } catch (error) {
            console.log("Erreur lors de la récupération de la liste.", error);
        } finally {
            loading = false;
        }
    })

    function posNeg(percent) {
    if (percent >= 0) {
        return 'green';  // Retourne "green" si positif
    } else {
        return 'red';  // Retourne "red" si négatif
    }
}

</script>

{#if loading}
    <p>Chargement...</p>
{:else}
<table>
    <thead>
        <tr>
            <th>N°</th>
            <th>Nom</th>
            <th>Prix</th>                    
            <th>% in 1H</th>
            <th>% in 24H</th>                        
            <th>% in 30D</th>
        </tr>
    </thead>
    <tbody>
        {#each coinList as coin}
            <tr>
                <td>{coin.cmc_rank}</td>
                <td>{coin.name}</td>
                <td>{coin.quote.USD.price.toFixed(2)} $</td>
                <!-- Appliquer la couleur en fonction du signe -->
                <td style="color: {posNeg(coin.quote.USD.percent_change_1h)};">
                    {coin.quote.USD.percent_change_1h.toFixed(2)} %
                </td>
                <td style="color: {posNeg(coin.quote.USD.percent_change_24h)};">
                    {coin.quote.USD.percent_change_24h.toFixed(2)} %
                </td>
                <td style="color: {posNeg(coin.quote.USD.percent_change_30d)};">
                    {coin.quote.USD.percent_change_30d.toFixed(2)} %
                </td>
            </tr>
        {/each}
    </tbody>
</table>
{/if}


<style>

table {
    width: 100%;
    border-collapse: separate;  /* Permet de créer un espacement entre les lignes */
    border-spacing: 0 5px;      /* Espacement entre les lignes verticalement */
}

th, td {
    width: 200px;
    padding: 10px;
    text-align: center;
    border: 1px solid #ffffff00;   /* Bordure visible */
}

th {
    background-color: #ffffff00;
    font-weight: bold;
    
}

td {
    font-size: 0.9rem;
    
}

tr {
    box-shadow: 3px 3px 5px 0px rgba(0, 0, 0, 0.28);
    padding: 10px;
}


    
</style>
