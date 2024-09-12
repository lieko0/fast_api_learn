import ClienteForm from '../ui/cliente/ClienteForm';

export default function NewClientePage() {
  return (
    <div>
      <h1>Novo Cliente</h1>
      <ClienteForm clienteId={null} />
    </div>
  );
}
