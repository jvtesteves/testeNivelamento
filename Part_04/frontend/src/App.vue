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
        <li
            v-for="(op, index) in resultados"
            :key="index"
            class="card"
            @click="toggle(index)"
        >
          <strong>{{ op["Nome_Fantasia"] || 'Sem nome fantasia' }}</strong><br />
          {{ op["Razao_Social"] || 'Razão social indisponível' }}<br />
          CNPJ: {{ op["CNPJ"] || '---' }} | Registro ANS: {{ op["Registro_ANS"] || '---' }}<br />
          UF: {{ op["UF"] || '--' }} | Cidade: {{ op["Cidade"] || '--' }}

          <transition name="fade">
            <div v-if="expandedIndex === index" class="detalhes">
              <hr />
              <p><strong>Modalidade:</strong> {{ op["Modalidade"] || '---' }}</p>
              <p><strong>Endereço:</strong> {{ op["Logradouro"] || '' }}, Nº {{ op["Numero"] || '' }} {{ op["Complemento"] || '' }}</p>
              <p><strong>Bairro:</strong> {{ op["Bairro"] || '---' }} - <strong>CEP:</strong> {{ op["CEP"] || '---' }}</p>
              <p><strong>DDD:</strong> {{ op["DDD"] || '---' }} | <strong>Telefone:</strong> {{ op["Telefone"] || '---' }} | <strong>Fax:</strong> {{ op["Fax"] || '---' }}</p>
              <p><strong>Email:</strong> {{ op["Endereco_eletronico"] || '---' }}</p>
              <p><strong>Representante:</strong> {{ op["Representante"] || '---' }} ({{ op["Cargo_Representante"] || '---' }})</p>
              <p><strong>Região de Comercialização:</strong> {{ op["Regiao_de_Comercializacao"] || '---' }}</p>
              <p><strong>Data de Registro ANS:</strong> {{ op["Data_Registro_ANS"] || '---' }}</p>
            </div>
          </transition>
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
      buscou: false,
      expandedIndex: null
    }
  },
  methods: {
    async buscar() {
      if (!this.busca.trim()) return

      try {
        const response = await axios.get(`http://localhost:5000/buscar-operadoras?query=${this.busca}`)
        this.resultados = response.data
        this.buscou = true
        this.expandedIndex = null // Reset ao buscar de novo
      } catch (error) {
        console.error('Erro ao buscar:', error)
        this.resultados = []
        this.buscou = true
      }
    },
    toggle(index) {
      this.expandedIndex = this.expandedIndex === index ? null : index
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

.container {
  max-width: 800px;
  margin: 60px auto;
  padding: 20px;
  font-family: 'Inter', sans-serif;
}

h1 {
  font-size: 2rem;
  color: #2c3e50;
  margin-bottom: 25px;
}

.search-area {
  display: flex;
  gap: 10px;
  margin-bottom: 30px;
}

input {
  flex: 1;
  padding: 12px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 6px;
  transition: border 0.3s;
}

input:focus {
  border-color: #3498db;
  outline: none;
}

button {
  padding: 12px 20px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #2980b9;
  cursor: pointer;
}

ul {
  list-style-type: none;
  padding-left: 0;
}

.card {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 15px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition: all 0.3s;
}

.card:hover {
  background-color: #eef6fc;
  cursor: pointer;
}

.card strong {
  font-size: 18px;
  color: #2c3e50;
}

.detalhes {
  margin-top: 10px;
  font-size: 14px;
  line-height: 1.6;
}

.fade-enter-active, .fade-leave-active {
  transition: all 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: scaleY(0.95);
}
</style>
