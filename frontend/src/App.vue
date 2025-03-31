<template>
  <div class="container">
    <h1>Buscar Operadoras da ANS</h1>
    <div class="search-area">
      <input v-model="busca" @keyup.enter="buscar" placeholder="Digite um nome, CNPJ ou registro ANS" />
      <button @click="buscar">Buscar</button>
    </div>

    <div v-if="resultados.length">
      <h2>Resultados:</h2>
      <ul>
        <li v-for="(op, index) in resultados" :key="index">
          <strong>{{ op["Nome_Fantasia"] || 'Sem nome fantasia' }}</strong><br />
          {{ op["Razao_Social"] || 'Razão social indisponível' }}<br />
          CNPJ: {{ op["CNPJ"] || '---' }} | Registro ANS: {{ op["Registro_ANS"] || '---' }}<br />
          UF: {{ op["UF"] || '--' }} | Cidade: {{ op["Cidade"] || '--' }}
        </li>
      </ul>
    </div>

    <div v-else-if="buscou">
      <p>Nenhum resultado encontrado.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      busca: '',
      resultados: [],
      buscou: false
    }
  },
  methods: {
    async buscar() {
      if (!this.busca.trim()) return

      try {
        const response = await axios.get(`http://localhost:5000/buscar-operadoras?query=${this.busca}`)
        console.log(response.data)  // <- ADICIONE ISSO
        this.resultados = response.data
        this.buscou = true
      } catch (error) {
        console.error('Erro ao buscar:', error)
        this.resultados = []
        this.buscou = true
      }
    }
  }
}
</script>

<style scoped>
.container {
  max-width: 700px;
  margin: 40px auto;
  font-family: Arial, sans-serif;
}
.search-area {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}
input {
  flex: 1;
  padding: 8px;
  font-size: 16px;
}
button {
  padding: 8px 16px;
  font-size: 16px;
  cursor: pointer;
}
ul {
  list-style-type: none;
  padding-left: 0;
}
li {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}
</style>
