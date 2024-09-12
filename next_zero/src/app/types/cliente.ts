export interface Cliente {
    id: number;
    nome: string;
    cpf: string;
    data_nasc: string;  // formato 'YYYY-MM-DD'
    email: string;
  }
  
  export interface ClienteCreate {
    nome: string;
    cpf: string;
    data_nasc: string;
    email: string;
  }
  