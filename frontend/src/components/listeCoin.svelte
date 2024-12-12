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
        return '#A3F23E';  // Retourne "green" si positif
    } else {
        return '#F23E5A';  // Retourne "red" si négatif
    }
}

</script>

{#if loading}
    <p>Chargement...</p>
{:else}

    <div class="table">
        <div class="table-header">
            <div class="table-cell">N°</div>
            <div class="table-cell">Nom</div>
            <div class="table-cell">Prix</div>
            <div class="table-cell">% in 1H</div>
            <div class="table-cell">% in 24H</div>
            <div class="table-cell">% in 30D</div>
        </div>
        {#each coinList as coin}
            <div class="table-row">
                <div class="table-cell" data-label="N°">{coin.cmc_rank}</div>
                <div class="table-cell" data-label="Nom">{coin.name}</div>
                <div class="table-cell" data-label="Prix">{coin.quote.USD.price.toFixed(2)} $</div>
                <div class="table-cell" data-label="Prix" style="color: {posNeg(coin.quote.USD.percent_change_1h)};">{coin.quote.USD.percent_change_1h.toFixed(2)} %</div>
                  
                <div class="table-cell" data-label="Prix" style="color: {posNeg(coin.quote.USD.percent_change_1h)};">{coin.quote.USD.percent_change_24h.toFixed(2)} %</div>
                <div class="table-cell" data-label="Prix" style="color: {posNeg(coin.quote.USD.percent_change_1h)};">{coin.quote.USD.percent_change_30d.toFixed(2)} %</div>

            </div>
        {/each}
    </div>

{/if}


<style>
.table {
    display: flex;
    flex-direction: column;
    width: 100%;
    background-color: rgba(255, 255, 255, 0);
    border-radius: 8px;
}

.table-header {
    display: flex;
    justify-content: space-between;
    padding: 12px;
    border-bottom: 1px solid #dddddd00;
    font-weight: bold;
    font-family: Jaldi, sans-serif;
    color: #A3F23E;
}

.table-row {
    height: 40PX;
    display: flex;
    border-radius: 12px;
    justify-content: space-between;
    align-items: center;
    margin: 5px;
    padding: 12px;
    background-color: #323232;
    border: 1px solid #70707050;
    box-shadow: 3px 3px 5px 0px rgba(0, 0, 0, 0.3);
    font-family: Jaldi, sans-serif;
    color: #fff;
}

.table-cell {
    flex: 1;
    text-align: left;
    padding: 10px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.table-row:hover {
    background-color: #222222;
}

@media (max-width: 768px) {
    .table {
        display: block;
        overflow-x: auto;
        white-space: nowrap;
    }
    .table-header {
        display: none;
    }
    .table-row {
        display: block;
    }
    .table-cell {
        display: block;
        text-align: right;
    }
    .table-cell::before {
        content: attr(data-label);
        font-weight: bold;
        float: left;
    }
}

</style>
