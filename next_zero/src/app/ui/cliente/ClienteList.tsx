'use client'

import { useEffect, useState } from 'react';
import { getClientes, deleteCliente } from '../../services/clienteService';
import { Cliente } from '../../types/cliente';
import Link from 'next/link';

export default function ClienteList() {
  const [clientes, setClientes] = useState<Cliente[]>([]);

  useEffect(() => {
    const fetchClientes = async () => {
      const data = await getClientes();
      // console.log(data.data.clientes)
      setClientes(data.data.clientes);
    };
    fetchClientes();
  }, []);

  const handleDelete = async (id: number) => {
    await deleteCliente(id);
    setClientes(clientes.filter((cliente) => cliente.id !== id));
  };

  return (
    <div>
      <h1>Clientes</h1>
      <ul>
       
       {clientes.map((cliente) => (
          <li key={cliente.id}>
            {cliente.nome} - {cliente.cpf}
            <Link href={`/cliente/${cliente.id}`}>Editar</Link>
            <button onClick={() => handleDelete(cliente.id)}>Deletar</button>
          </li>
        ))} 
      
      </ul>
    </div>
  );
}
