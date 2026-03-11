import Head from 'next/head';
import Layout from '../components/Layout';

export default function Home() {
  return (
    <Layout>
      <Head>
        <title>TaskMaster Pro</title>
      </Head>
      <div className="p-4">
        <h1 className="text-2xl font-bold">Welcome to TaskMaster Pro</h1>
        <p className="mt-2">Your productivity companion.</p>
      </div>
    </Layout>
  );
}