import axios from 'axios';
import { Cliente, ClienteCreate } from '../types/cliente';

const API_URL = 'http://localhost:8000/clientes/';

export const getClientes = async (skip = 0, limit = 100): Promise<any> => {
    const response = await axios.get(`${API_URL}?skip=${skip}&limit=${limit}`);
    return response;
};

export const getClienteById = async (id: number): Promise<Cliente> => {
  const response = await axios.get(`${API_URL}${id}`);
  return response.data;
};

export const createCliente = async (clienteData: ClienteCreate): Promise<Cliente> => {
  const response = await axios.post(API_URL, clienteData);
  return response.data;
};

export const updateCliente = async (id: number, clienteData: ClienteCreate): Promise<Cliente> => {
  const response = await axios.put(`${API_URL}${id}`, clienteData);
  return response.data;
};

export const deleteCliente = async (id: number): Promise<void> => {
  await axios.delete(`${API_URL}${id}`);
};

export const getClienteByCpf = async (cpf: string): Promise<Cliente> => {
  const response = await axios.get(`${API_URL}cpf/?cpf=${cpf}`);
  return response.data;
};
