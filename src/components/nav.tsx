import Link from "next/link";

const links = [
  { href: "/", label: "Home" },
  { href: "/services", label: "Services" },
  { href: "/about", label: "About" },
];

export default function Nav() {
  return (
    <header className="sticky top-0 z-50 border-b border-line bg-paper/90 backdrop-blur">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4 md:px-10">
        <Link
          href="/"
          className="font-mono text-sm font-medium tracking-[0.2em] uppercase"
        >
          Branding Agency
        </Link>

        <nav className="hidden items-center gap-8 md:flex">
          {links.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className="text-sm text-ink-soft transition-colors hover:text-ink"
            >
              {link.label}
            </Link>
          ))}
          <Link
            href="/contact"
            className="border border-ink px-4 py-1.5 text-sm transition-colors hover:bg-ink hover:text-paper"
          >
            Contact
          </Link>
        </nav>

        <details className="md:hidden">
          <summary className="cursor-pointer list-none text-sm">
            Menu
          </summary>
          <div className="absolute inset-x-0 top-full flex flex-col gap-1 border-b border-line bg-paper px-6 py-4">
            {[...links, { href: "/contact", label: "Contact" }].map(
              (link) => (
                <Link
                  key={link.href}
                  href={link.href}
                  className="py-2 text-sm text-ink-soft hover:text-ink"
                >
                  {link.label}
                </Link>
              ),
            )}
          </div>
        </details>
      </div>
    </header>
  );
}
