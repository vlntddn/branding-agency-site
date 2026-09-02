import type { ReactNode } from "react";

export function Container({ children }: { children: ReactNode }) {
  return <div className="mx-auto max-w-6xl px-6 md:px-10">{children}</div>;
}

export function Eyebrow({ children }: { children: ReactNode }) {
  return (
    <p className="font-mono text-xs tracking-[0.2em] text-signal uppercase">
      {children}
    </p>
  );
}

export function Index({ n }: { n: number }) {
  return (
    <span className="font-mono text-xs text-ink-soft">
      {String(n).padStart(2, "0")}
    </span>
  );
}
