import Link from 'next/link';

const Navbar: React.FC = () => {
  return (
    <nav className="bg-blue-600 fixed w-full z-10">
      <div className="container mx-auto px-4 py-3">
        <div className="flex justify-between">
          <Link href="/">
            <a className="text-white text-lg font-bold">TaskMaster Pro</a>
          </Link>
          <div>
            <Link href="/tasks">
              <a className="text-white ml-4">Tasks</a>
            </Link>
            <Link href="/categories">
              <a className="text-white ml-4">Categories</a>
            </Link>
            <Link href="/auth/login">
              <a className="text-white ml-4">Login</a>
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;