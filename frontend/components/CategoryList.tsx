import { Category } from '../lib/types';

interface CategoryListProps {
  categories: Category[];
}

const CategoryList: React.FC<CategoryListProps> = ({ categories }) => {
  if (categories.length === 0) return <p>No categories available.</p>;

  return (
    <ul className="divide-y divide-gray-200">
      {categories.map(category => (
        <li key={category.id} className="p-4 hover:bg-gray-50">
          <h3 className="text-lg font-bold">{category.name}</h3>
        </li>
      ))}
    </ul>
  );
};

export default CategoryList;