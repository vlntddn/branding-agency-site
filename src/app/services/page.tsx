import Link from "next/link";
import type { Metadata } from "next";
import { Container, Eyebrow, Index } from "@/components/ui";

export const metadata: Metadata = {
  title: "Services",
  description:
    "Brand strategy, naming, visual identity systems, and guidelines — built as a system, not a style.",
};

const services = [
  {
    title: "Brand strategy & positioning",
    body: "Before design starts, we define what you stand for, who it's for, and what you're willing not to be. Everything downstream traces back to this.",
    deliverables: [
      "Positioning statement",
      "Audience & competitive landscape",
      "Messaging pillars",
    ],
  },
  {
    title: "Naming & verbal identity",
    body: "A name and vocabulary that survive contact with a trademark search, a pitch deck, and a support ticket — in that order.",
    deliverables: [
      "Name candidates & screening",
      "Tagline & tone of voice",
      "Verbal identity guide",
    ],
  },
  {
    title: "Visual identity systems",
    body: "Mark, type, color, and layout logic, built as a system with explicit rules — not a one-off logo file.",
    deliverables: [
      "Logo & mark system",
      "Type & color specification",
      "Applied templates",
    ],
  },
  {
    title: "Brand guidelines & rollout",
    body: "Documentation your team, agency, and vendors can apply correctly without asking you first.",
    deliverables: [
      "Guidelines document",
      "Asset library & tokens",
      "Rollout support",
    ],
  },
];

const process = [
  { step: "Discover", body: "Interviews, audits, and research into what's actually true about the brand." },
  { step: "Define", body: "Strategy and positioning, written down and agreed before any visual work begins." },
  { step: "Design", body: "Systems built and stress-tested across real applications, not just a hero shot." },
  { step: "Deliver", body: "Documentation and handoff so the system holds up without us in the room." },
];

export default function Services() {
  return (
    <>
      <section className="border-b border-line py-20">
        <Container>
          <Eyebrow>Services</Eyebrow>
          <h1 className="mt-3 max-w-2xl text-3xl font-medium tracking-tight md:text-5xl">
            Four disciplines. One system.
          </h1>
          <p className="mt-6 max-w-xl text-ink-soft">
            We take on strategy, naming, identity, and guidelines together
            or standalone — depending on how much of the system already
            exists.
          </p>
        </Container>
      </section>

      <section className="border-b border-line py-16">
        <Container>
          <div className="divide-y divide-line border-t border-line">
            {services.map((s, i) => (
              <div key={s.title} className="grid gap-6 py-10 md:grid-cols-12">
                <div className="md:col-span-1">
                  <Index n={i + 1} />
                </div>
                <div className="md:col-span-5">
                  <h2 className="text-xl font-medium">{s.title}</h2>
                  <p className="mt-3 text-sm text-ink-soft">{s.body}</p>
                </div>
                <div className="md:col-span-5 md:col-start-8">
                  <p className="font-mono text-xs tracking-[0.2em] text-ink-soft uppercase">
                    What you get
                  </p>
                  <ul className="mt-3 space-y-2 text-sm">
                    {s.deliverables.map((d) => (
                      <li key={d} className="flex gap-3">
                        <span className="text-signal">—</span>
                        {d}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            ))}
          </div>
        </Container>
      </section>

      <section className="border-b border-line py-20">
        <Container>
          <Eyebrow>How we work</Eyebrow>
          <h2 className="mt-3 text-2xl font-medium tracking-tight md:text-3xl">
            The same four steps, every time.
          </h2>
          <div className="mt-12 grid gap-px overflow-hidden border border-line bg-line md:grid-cols-4">
            {process.map((p, i) => (
              <div key={p.step} className="bg-paper p-6">
                <Index n={i + 1} />
                <h3 className="mt-2 text-base font-medium">{p.step}</h3>
                <p className="mt-2 text-sm text-ink-soft">{p.body}</p>
              </div>
            ))}
          </div>
        </Container>
      </section>

      <section className="bg-ink py-16 text-paper">
        <Container>
          <div className="flex flex-col items-start justify-between gap-6 md:flex-row md:items-center">
            <h2 className="max-w-lg text-2xl font-medium tracking-tight md:text-3xl">
              Not sure which service you need?
            </h2>
            <Link
              href="/contact"
              className="shrink-0 bg-signal px-5 py-3 text-sm text-paper transition-colors hover:bg-paper hover:text-ink"
            >
              Tell us about the brand
            </Link>
          </div>
        </Container>
      </section>
    </>
  );
}
