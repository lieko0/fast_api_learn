import ClienteList from './ui/cliente/ClienteList';
import Link from 'next/link';

export default function Home() {
  return (
    <div>
      <h1>Gerenciamento de Clientes</h1>
      <Link href="/cliente/new">Novo Cliente</Link>
      <ClienteList />
    </div>
  );
}
