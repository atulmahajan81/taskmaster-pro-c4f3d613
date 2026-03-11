import TaskItem from './TaskItem';
import { Task } from '../lib/types';

interface TaskListProps {
  tasks: Task[];
}

const TaskList: React.FC<TaskListProps> = ({ tasks }) => {
  if (tasks.length === 0) return <p>No tasks available.</p>;

  return (
    <ul className="divide-y divide-gray-200">
      {tasks.map(task => (
        <TaskItem key={task.id} task={task} />
      ))}
    </ul>
  );
};

export default TaskList;