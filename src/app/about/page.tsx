import Link from "next/link";
import type { Metadata } from "next";
import { Container, Eyebrow, Index } from "@/components/ui";

export const metadata: Metadata = {
  title: "About",
  description:
    "Why we're named exactly what we are, and how a small, senior team approaches brand work.",
};

const values = [
  {
    title: "Precision over aesthetics",
    body: "A trend-driven look expires. A precise decision — about audience, tone, and system — doesn't.",
  },
  {
    title: "Direct over decorative",
    body: "We'd rather say the true thing plainly than dress up a vague thing well.",
  },
  {
    title: "Senior on every project",
    body: "No handoff to a junior team once the pitch is won. The people you meet are the people who do the work.",
  },
];

export default function About() {
  return (
    <>
      <section className="border-b border-line py-20">
        <Container>
          <Eyebrow>About</Eyebrow>
          <h1 className="mt-3 max-w-2xl text-3xl font-medium tracking-tight md:text-5xl">
            Why we&apos;re called Branding Agency.
          </h1>
          <p className="mt-6 max-w-2xl text-ink-soft">
            Not because we ran out of imagination — because we&apos;d
            rather earn distinctiveness through the work than through a
            clever name. It&apos;s the same argument we make to clients:
            say exactly what you mean, and let the precision be the
            differentiator.
          </p>
        </Container>
      </section>

      <section className="border-b border-line py-20">
        <Container>
          <div className="grid gap-10 md:grid-cols-12">
            <div className="md:col-span-6">
              <Eyebrow>Mission</Eyebrow>
              <h2 className="mt-3 text-2xl font-medium tracking-tight md:text-3xl">
                Style is not aesthetics. It&apos;s precision.
              </h2>
              <p className="mt-4 text-ink-soft">
                We help brands and people say exactly what they mean — in
                the mark, the message, and everything in between. That
                means treating identity as a system of decisions, not a
                collection of assets, and being willing to leave things
                out until they earn their place.
              </p>
            </div>
            <div className="md:col-span-5 md:col-start-8">
              <Eyebrow>The studio</Eyebrow>
              <h2 className="mt-3 text-2xl font-medium tracking-tight md:text-3xl">
                Small, senior, newly founded.
              </h2>
              <p className="mt-4 text-ink-soft">
                We&apos;re a small studio built deliberately to stay small
                — every project gets senior attention from strategy
                through delivery, not a rotating cast. Team page and case
                studies are coming as we take on our first engagements.
              </p>
            </div>
          </div>
        </Container>
      </section>

      <section className="border-b border-line py-20">
        <Container>
          <Eyebrow>What we value</Eyebrow>
          <h2 className="mt-3 text-2xl font-medium tracking-tight md:text-3xl">
            Three things we won&apos;t compromise on.
          </h2>
          <div className="mt-12 grid gap-10 md:grid-cols-3">
            {values.map((v, i) => (
              <div key={v.title} className="border-t border-line pt-5">
                <Index n={i + 1} />
                <h3 className="mt-2 text-base font-medium">{v.title}</h3>
                <p className="mt-2 text-sm text-ink-soft">{v.body}</p>
              </div>
            ))}
          </div>
        </Container>
      </section>

      <section className="bg-ink py-16 text-paper">
        <Container>
          <div className="flex flex-col items-start justify-between gap-6 md:flex-row md:items-center">
            <h2 className="max-w-lg text-2xl font-medium tracking-tight md:text-3xl">
              Want to work with us?
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
