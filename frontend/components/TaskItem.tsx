import { Task } from '../lib/types';

interface TaskItemProps {
  task: Task;
}

const TaskItem: React.FC<TaskItemProps> = ({ task }) => {
  return (
    <li className="p-4 hover:bg-gray-50">
      <div className="flex justify-between">
        <div>
          <h3 className="text-lg font-bold">{task.title}</h3>
          <p className="text-sm text-gray-500">Due: {task.dueDate}</p>
        </div>
        <p className="text-sm text-gray-500">Priority: {task.priority}</p>
      </div>
    </li>
  );
};

export default TaskItem;