import type { Metadata } from "next";
import { Container, Eyebrow, Index } from "@/components/ui";

export const metadata: Metadata = {
  title: "Contact",
  description: "Start a project or ask a question — reach us directly.",
};

const steps = [
  {
    title: "You write in",
    body: "A few lines on the brand, the problem, and rough timing is enough to start.",
  },
  {
    title: "We reply within 2 business days",
    body: "With questions if we need them, or a straight yes/no on fit.",
  },
  {
    title: "We scope together",
    body: "A short call to size the work and agree what a good outcome looks like.",
  },
];

export default function Contact() {
  return (
    <>
      <section className="border-b border-line py-20">
        <Container>
          <Eyebrow>Contact</Eyebrow>
          <h1 className="mt-3 max-w-2xl text-3xl font-medium tracking-tight md:text-5xl">
            Tell us about the brand.
          </h1>
          <p className="mt-6 max-w-xl text-ink-soft">
            No form to fill in triplicate. Email directly and we&apos;ll
            take it from there.
          </p>
        </Container>
      </section>

      <section className="py-16">
        <Container>
          <div className="grid gap-10 md:grid-cols-12">
            <div className="md:col-span-6">
              <p className="font-mono text-xs tracking-[0.2em] text-ink-soft uppercase">
                Email
              </p>
              <a
                href="mailto:valentinddn2803@gmail.com"
                className="mt-2 inline-block text-2xl font-medium tracking-tight hover:text-signal md:text-3xl"
              >
                valentinddn2803@gmail.com
              </a>

              <p className="mt-10 font-mono text-xs tracking-[0.2em] text-ink-soft uppercase">
                Based
              </p>
              <p className="mt-2 text-lg">Remote-first, worldwide</p>

              <p className="mt-10 text-xs text-ink-soft">
                Contact details are placeholder pending CEO sign-off on a
                dedicated inbox and domain.
              </p>
            </div>

            <div className="md:col-span-5 md:col-start-8">
              <p className="font-mono text-xs tracking-[0.2em] text-ink-soft uppercase">
                What happens next
              </p>
              <div className="mt-4 space-y-6 border-t border-line pt-6">
                {steps.map((s, i) => (
                  <div key={s.title} className="flex gap-4">
                    <Index n={i + 1} />
                    <div>
                      <h3 className="text-sm font-medium">{s.title}</h3>
                      <p className="mt-1 text-sm text-ink-soft">{s.body}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </Container>
      </section>
    </>
  );
}
