export default function NavBar() {
  return (
    <nav className="bg-gray-900 text-white p-4">
      <div className="container mx-auto flex justify-between">
        <span className="font-bold text-xl">Code Cracker</span>
        <div className="space-x-4">
          <a href="/" className="hover:underline">Dashboard</a>
          <a href="/profile" className="hover:underline">Profile</a>
        </div>
      </div>
    </nav>
  );
}
