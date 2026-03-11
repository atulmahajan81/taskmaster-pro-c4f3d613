import Layout from '../../components/Layout';
import TaskList from '../../components/TaskList';
import { useTasks } from '../../lib/hooks/useTasks';

export default function Tasks() {
  const { data, isLoading, isError } = useTasks();

  if (isLoading) return <p>Loading tasks...</p>;
  if (isError) return <p>Error loading tasks.</p>;

  return (
    <Layout>
      <div className="p-4">
        <h1 className="text-2xl font-bold">Tasks</h1>
        <TaskList tasks={data?.tasks || []} />
      </div>
    </Layout>
  );
}