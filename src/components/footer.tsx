import Link from "next/link";

export default function Footer() {
  return (
    <footer className="border-t border-line">
      <div className="mx-auto max-w-6xl px-6 py-12 md:px-10">
        <div className="grid gap-10 md:grid-cols-3">
          <div>
            <p className="font-mono text-sm tracking-[0.2em] uppercase">
              Branding Agency
            </p>
            <p className="mt-3 max-w-xs text-sm text-ink-soft">
              Style is not aesthetics. It&apos;s precision.
            </p>
          </div>

          <div>
            <p className="font-mono text-xs tracking-[0.2em] text-ink-soft uppercase">
              Site
            </p>
            <ul className="mt-3 space-y-2 text-sm">
              <li>
                <Link href="/" className="hover:text-signal">
                  Home
                </Link>
              </li>
              <li>
                <Link href="/services" className="hover:text-signal">
                  Services
                </Link>
              </li>
              <li>
                <Link href="/about" className="hover:text-signal">
                  About
                </Link>
              </li>
              <li>
                <Link href="/contact" className="hover:text-signal">
                  Contact
                </Link>
              </li>
            </ul>
          </div>

          <div>
            <p className="font-mono text-xs tracking-[0.2em] text-ink-soft uppercase">
              Get in touch
            </p>
            <ul className="mt-3 space-y-2 text-sm">
              <li>
                <a
                  href="mailto:hello@brandingagency.co"
                  className="hover:text-signal"
                >
                  hello@brandingagency.co
                </a>
              </li>
              <li className="text-ink-soft">Remote-first, worldwide</li>
            </ul>
          </div>
        </div>

        <div className="mt-10 flex flex-col gap-2 border-t border-line pt-6 text-xs text-ink-soft sm:flex-row sm:items-center sm:justify-between">
          <p>&copy; {new Date().getFullYear()} Branding Agency. All rights reserved.</p>
          <p>Site copy is placeholder, pending CEO review.</p>
        </div>
      </div>
    </footer>
  );
}
