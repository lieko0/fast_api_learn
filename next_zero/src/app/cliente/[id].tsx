import { useRouter } from 'next/router';
import ClienteForm from '../ui/cliente/ClienteForm';

export default function ClientePage() {
  const router = useRouter();
  const { id } = router.query;

  const clienteId = id === 'new' ? null : Number(id);

  return (
    <div>
      <h1>Editar Cliente</h1>
      <ClienteForm clienteId={clienteId} />
    </div>
  );
}
