import Layout from '../../components/Layout';
import CategoryList from '../../components/CategoryList';
import { useCategories } from '../../lib/hooks/useCategories';

export default function Categories() {
  const { data, isLoading, isError } = useCategories();

  if (isLoading) return <p>Loading categories...</p>;
  if (isError) return <p>Error loading categories.</p>;

  return (
    <Layout>
      <div className="p-4">
        <h1 className="text-2xl font-bold">Categories</h1>
        <CategoryList categories={data?.categories || []} />
      </div>
    </Layout>
  );
}