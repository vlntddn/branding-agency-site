import Link from "next/link";
import { Container, Eyebrow, Index } from "@/components/ui";

const principles = [
  {
    title: "Say less, mean more",
    body: "Every mark, line, and page earns its place. If it doesn't carry meaning, it doesn't ship.",
  },
  {
    title: "Systems, not styles",
    body: "We build rules a brand can run on for years, not a moodboard that dates in one.",
  },
  {
    title: "Legible under pressure",
    body: "A brand should still be unmistakable at 16px, in grayscale, or read aloud over the phone.",
  },
];

const services = [
  {
    title: "Brand strategy & positioning",
    body: "Define what you stand for and who it's for, before a single pixel moves.",
  },
  {
    title: "Naming & verbal identity",
    body: "A name, tone, and vocabulary that hold up in a pitch, a support ticket, and a tagline.",
  },
  {
    title: "Visual identity systems",
    body: "Mark, type, color, and layout logic — built as a system, not a one-off.",
  },
  {
    title: "Guidelines & rollout",
    body: "Documentation your team and vendors can actually apply without asking you first.",
  },
];

export default function Home() {
  return (
    <>
      <section className="border-b border-line">
        <Container>
          <div className="grid gap-10 py-20 md:grid-cols-12 md:py-28">
            <div className="md:col-span-8">
              <Eyebrow>Branding Agency — 001</Eyebrow>
              <h1 className="mt-4 text-4xl leading-[1.05] font-medium tracking-tight md:text-6xl">
                Style is not aesthetics.
                <br />
                It&apos;s precision.
              </h1>
              <p className="mt-6 max-w-xl text-lg text-ink-soft">
                We help brands and people say exactly what they mean — in
                the mark, the message, and everything in between.
              </p>
              <div className="mt-8 flex flex-wrap gap-4">
                <Link
                  href="/contact"
                  className="bg-ink px-5 py-3 text-sm text-paper transition-colors hover:bg-signal"
                >
                  Start a project
                </Link>
                <Link
                  href="/services"
                  className="border border-ink px-5 py-3 text-sm transition-colors hover:bg-ink hover:text-paper"
                >
                  See our services
                </Link>
              </div>
            </div>
          </div>
        </Container>
      </section>

      <section className="border-b border-line py-20">
        <Container>
          <Eyebrow>Our thesis</Eyebrow>
          <h2 className="mt-3 max-w-2xl text-2xl font-medium tracking-tight md:text-3xl">
            Decoration fades. Precision compounds.
          </h2>
          <div className="mt-12 grid gap-10 md:grid-cols-3">
            {principles.map((p, i) => (
              <div key={p.title} className="border-t border-line pt-5">
                <Index n={i + 1} />
                <h3 className="mt-2 text-base font-medium">{p.title}</h3>
                <p className="mt-2 text-sm text-ink-soft">{p.body}</p>
              </div>
            ))}
          </div>
        </Container>
      </section>

      <section className="border-b border-line py-20">
        <Container>
          <div className="flex flex-wrap items-end justify-between gap-4">
            <div>
              <Eyebrow>What we do</Eyebrow>
              <h2 className="mt-3 text-2xl font-medium tracking-tight md:text-3xl">
                Four disciplines, one system.
              </h2>
            </div>
            <Link
              href="/services"
              className="text-sm text-ink-soft hover:text-signal"
            >
              Full breakdown &rarr;
            </Link>
          </div>
          <div className="mt-12 grid gap-px overflow-hidden border border-line bg-line md:grid-cols-2">
            {services.map((s, i) => (
              <div key={s.title} className="bg-paper p-6 md:p-8">
                <Index n={i + 1} />
                <h3 className="mt-2 text-base font-medium">{s.title}</h3>
                <p className="mt-2 text-sm text-ink-soft">{s.body}</p>
              </div>
            ))}
          </div>
        </Container>
      </section>

      <section className="py-20">
        <Container>
          <div className="grid gap-10 md:grid-cols-12">
            <div className="md:col-span-7">
              <Eyebrow>About</Eyebrow>
              <h2 className="mt-3 text-2xl font-medium tracking-tight md:text-3xl">
                A small, senior team that ships systems, not decks.
              </h2>
              <p className="mt-4 max-w-xl text-ink-soft">
                We&apos;re a newly founded studio built around one idea: a
                brand is a set of precise decisions, not a look. Read more
                about how we work and why we&apos;re named exactly what we
                are.
              </p>
              <Link
                href="/about"
                className="mt-6 inline-block border border-ink px-5 py-3 text-sm transition-colors hover:bg-ink hover:text-paper"
              >
                About the studio
              </Link>
            </div>
          </div>
        </Container>
      </section>

      <section className="border-t border-line bg-ink py-16 text-paper">
        <Container>
          <div className="flex flex-col items-start justify-between gap-6 md:flex-row md:items-center">
            <h2 className="max-w-lg text-2xl font-medium tracking-tight md:text-3xl">
              Have a brand that needs precision?
            </h2>
            <Link
              href="/contact"
              className="shrink-0 bg-signal px-5 py-3 text-sm text-paper transition-colors hover:bg-paper hover:text-ink"
            >
              Get in touch
            </Link>
          </div>
        </Container>
      </section>
    </>
  );
}
