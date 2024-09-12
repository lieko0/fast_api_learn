'use client'

import { useState, useEffect } from 'react';
import { createCliente, getClienteById, updateCliente } from '../../services/clienteService';
import { ClienteCreate, Cliente } from '../../types/cliente';
import { useRouter } from 'next/router';

interface ClienteFormProps {
  clienteId?: number | null;
}

export default function ClienteForm({ clienteId }: ClienteFormProps) {
  const [cliente, setCliente] = useState<ClienteCreate>({
    nome: '',
    cpf: '',
    data_nasc: '',
    email: ''
  });

  const router = useRouter();

  useEffect(() => {
    if (clienteId) {
      const fetchCliente = async () => {
        const data: Cliente = await getClienteById(clienteId);
        setCliente({
          nome: data.nome,
          cpf: data.cpf,
          data_nasc: data.data_nasc,
          email: data.email
        });
      };
      fetchCliente();
    }
  }, [clienteId]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (clienteId) {
      await updateCliente(clienteId, cliente);
    } else {
      await createCliente(cliente);
    }
    router.push('/');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Nome"
        value={cliente.nome}
        onChange={(e) => setCliente({ ...cliente, nome: e.target.value })}
        required
      />
      <input
        type="text"
        placeholder="CPF"
        value={cliente.cpf}
        onChange={(e) => setCliente({ ...cliente, cpf: e.target.value })}
        required
      />
      <input
        type="date"
        placeholder="Data de Nascimento"
        value={cliente.data_nasc}
        onChange={(e) => setCliente({ ...cliente, data_nasc: e.target.value })}
        required
      />
      <input
        type="email"
        placeholder="Email"
        value={cliente.email}
        onChange={(e) => setCliente({ ...cliente, email: e.target.value })}
        required
      />
      <button type="submit">{clienteId ? 'Atualizar' : 'Criar'}</button>
    </form>
  );
}
